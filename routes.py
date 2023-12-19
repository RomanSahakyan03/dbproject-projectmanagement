from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_project, read_all_projects, read_all_workers, read_project, read_projects_with_conditions, read_projects_with_workers, update_project, delete_project
from crud import create_worker, read_worker, update_worker, delete_worker
from crud import create_assignment, read_assignment, update_assignment, delete_assignment
from db_dependencies import get_db
from schemas import *

project_router = APIRouter() 


@project_router.post("/projects/", response_model=dict)
def create_project_route(project: dict, db: Session = Depends(get_db)):
    return create_project(db=db, project=project)

@project_router.get("/projects/{project_id}", response_model=dict)
def read_project_route(project_id: int, db: Session = Depends(get_db)):
    return read_project(db=db, project_id=project_id)

@project_router.get("/projects/", response_model=List[dict])
def get_all_projects(db: Session = Depends(get_db)):
    return read_all_projects(db=db)

@project_router.get("/projects/", response_model=list[dict])
def read_projects_with_conditions_route(
    name: str = Query(None, title="Project Name", description="Name of the project"),
    deadline: str = Query(None, title="Deadline", description="Deadline of the project"),
    db: Session = Depends(get_db)
):
    return read_projects_with_conditions(db=db, name=name, deadline=deadline)

@project_router.get("/projects/{project_id}/workers", response_model=list[dict])
def read_project_with_workers_route(project_id: int, db: Session = Depends(get_db)):
    return read_projects_with_workers(db=db, project_id=project_id)

@project_router.put("/projects/{project_id}", response_model=dict)
def update_project_route(project_id: int, updated_project: dict, db: Session = Depends(get_db)):
    return update_project(db=db, project_id=project_id, updated_project=updated_project)

@project_router.delete("/projects/{project_id}", response_model=dict)
def delete_project_route(project_id: int, db: Session = Depends(get_db)):
    return delete_project(db=db, project_id=project_id)


worker_router = APIRouter()


@worker_router.post("/workers/", response_model=dict)
def create_worker_route(worker: dict, db: Session = Depends(get_db)):
    return create_worker(db=db, worker=worker)

@worker_router.get("/workers/{worker_id}", response_model=dict)
def read_worker_route(worker_id: int, db: Session = Depends(get_db)):
    return read_worker(db=db, worker_id=worker_id)

@worker_router.get("/workers/", response_model=list[dict])
def get_workers(db: Session = Depends(get_db)):
    return read_all_workers(db=db)

@worker_router.put("/workers/{worker_id}", response_model=dict)
def update_worker_route(worker_id: int, updated_worker: dict, db: Session = Depends(get_db)):
    return update_worker(db=db, worker_id=worker_id, updated_worker=updated_worker)

@worker_router.delete("/workers/{worker_id}", response_model=dict)
def delete_worker_route(worker_id: int, db: Session = Depends(get_db)):
    return delete_worker(db=db, worker_id=worker_id)


assignment_router = APIRouter()


@assignment_router.post("/assignments/", response_model=AssignmentCreate)
def create_assignment_route(assignment: dict, db: Session = Depends(get_db)):
    return create_assignment(db=db, assignment=assignment)

@assignment_router.get("/assignments/{assignment_id}", response_model=AssignmentResponse)
def read_assignment_route(assignment_id: int, db: Session = Depends(get_db)):
    return read_assignment(db=db, assignment_id=assignment_id)

@assignment_router.put("/assignments/{assignment_id}", response_model=AssignmentCreate)
def update_assignment_route(assignment_id: int, updated_assignment: dict, db: Session = Depends(get_db)):
    return update_assignment(db=db, assignment_id=assignment_id, updated_assignment=updated_assignment)

@assignment_router.delete("/assignments/{assignment_id}", response_model=AssignmentResponse)
def delete_assignment_route(assignment_id: int, db: Session = Depends(get_db)):
    return delete_assignment(db=db, assignment_id=assignment_id)
