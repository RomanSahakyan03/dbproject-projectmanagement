from typing import List
from pydantic import BaseModel
from datetime import datetime

class ProjectCreate(BaseModel):
    name: str
    deadline: str
    workload: float
    code: int

class ProjectResponse(BaseModel):
    id: int
    name: str
    deadline: datetime
    workload: float
    code: int


class AssignmentCreate(BaseModel):
    issue_date: str
    full_completion_date: str
    actual_completion_date: str
    workload: float
    project_id: int
    worker_id: int

class AssignmentResponse(BaseModel):
    id: int
    issue_date: str
    full_completion_date: str
    actual_completion_date: str
    workload: float
    project: ProjectResponse
    worker_id: int

class WorkerCreate(BaseModel):
    position: str
    full_name: str
    identifier: str

class WorkerResponse(BaseModel):
    id: int
    position: str
    full_name: str
    identifier: str
    assignments: List[AssignmentResponse]
