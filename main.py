from fastapi import FastAPI
from routes import project_router, worker_router, assignment_router

app = FastAPI()

app.include_router(project_router, tags=["projects"])
app.include_router(worker_router, tags=["workers"])
app.include_router(assignment_router, tags=["assignments"])
