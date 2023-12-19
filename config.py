from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    database_name: str
    user: str
    password: str
    host: str = "localhost"

def load_config_from_env():
    database_name = os.getenv('DB_NAME', 'project_management')
    user = os.getenv('DB_USER', 'postgres')
    password = os.getenv('DB_PASSWORD', 'root')
    host = os.getenv('DB_HOST', 'localhost')

    return Config(database_name, user, password, host)
