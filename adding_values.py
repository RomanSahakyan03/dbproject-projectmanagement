import requests
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

BASE_URL = "http://localhost:8000"  # Replace with the actual URL of your FastAPI application

# Function to create a random project
def create_random_project():
    project_data = {
        "name": fake.word(),
        "deadline": (datetime.now() + timedelta(days=random.randint(1, 30))).isoformat(),
        "workload": random.uniform(10.0, 100.0),
        "code": random.randint(1000, 9999),
    }
    response = requests.post(f"{BASE_URL}/projects/", json=project_data)
    print("Project created:", response.json())

# Function to create a random worker
def create_random_worker():
    worker_data = {
        "position": fake.job(),
        "full_name": fake.name(),
        "identifier": fake.uuid4(),
    }
    response = requests.post(f"{BASE_URL}/workers/", json=worker_data)
    print("Worker created:", response.json())

# Function to create a random assignment
def create_random_assignment():
    projects_response = requests.get(f"{BASE_URL}/projects/")
    workers_response = requests.get(f"{BASE_URL}/workers/")

    try:
        projects_response.raise_for_status()
        workers_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
        return

    try:
        projects = projects_response.json()
        workers = workers_response.json()
    except requests.exceptions.JSONDecodeError as err:
        print(f"JSON decoding error: {err}")
        return

    if not projects or not workers:
        print("Error: Projects or workers list is empty.")
        return

    project_id = random.choice(projects)["id"]
    worker_id = random.choice(workers)["id"]

    assignment_data = {
        "issue_date": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
        "full_completion_date": (datetime.now() + timedelta(days=random.randint(1, 30))).isoformat(),
        "actual_completion_date": (datetime.now() + timedelta(days=random.randint(1, 30))).isoformat(),
        "workload": random.uniform(1.0, 20.0),
        "project_id": project_id,
        "worker_id": worker_id,
    }

    response = requests.post(f"{BASE_URL}/assignments/", json=assignment_data)

    try:
        response.raise_for_status()
        print("Assignment created:", response.json())
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")

# Generate random data and populate the database
# for _ in range(50):
#     create_random_project()

# for _ in range(20):
#     create_random_worker()

for _ in range(100):
    create_random_assignment()
