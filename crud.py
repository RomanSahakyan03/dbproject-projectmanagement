from datetime import datetime
from sqlalchemy import and_, select, update
from sqlalchemy.orm import Session, class_mapper
from sqlalchemy.exc import IntegrityError
from models import Project, Worker, Assignment
from fastapi import HTTPException

def create_project(db: Session, project: dict):
    try:
        # Only include columns defined in the Project model
        allowed_columns = ["name", "deadline", "workload", "code"]
        valid_project_data = {key: project[key] for key in allowed_columns if key in project}
        
        result = db.execute(Project.__table__.insert().values(valid_project_data))
        db.commit()
        return {"id": result.inserted_primary_key[0], **valid_project_data}
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Project with this code already exists",
        )

def row2dict(row):
    return {col.name: getattr(row, col.name) for col in class_mapper(row.__class__).mapped_table.c}

def read_project(db: Session, project_id: int):
    stmt = select(Project).where(Project.id == project_id)
    result = db.execute(stmt).scalar()
    if result:
        return row2dict(result)
    raise HTTPException(status_code=404, detail="Project not found")

def convert_project_to_dict(project):
    return {
        "id": project.id,
        "name": project.name,
        "deadline": project.deadline,
        "workload": project.workload,
        "code": project.code,
    }

def read_all_projects(db: Session):
    projects = db.query(Project).all()
    
    # Convert each Project instance to a dictionary
    return [convert_project_to_dict(project) for project in projects]

def update_project(db: Session, project_id: int, updated_project: dict):
    stmt = update(Project).where(Project.id == project_id).values(updated_project)
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    db.commit()
    return {**updated_project, "id": project_id}

def delete_project(db: Session, project_id: int):
    stmt = Project.__table__.delete().where(Project.id == project_id)
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    db.commit()
    return {"message": "Project deleted successfully"}

def create_worker(db: Session, worker: dict):
    try:
        result = db.execute(Worker.__table__.insert().values(worker))
        db.commit()
        return {"id": result.inserted_primary_key[0], **worker}
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Worker with this ID already exists",
        )

def read_worker(db: Session, worker_id: int):
    stmt = select(Worker).where(Worker.id == worker_id)
    result = db.execute(stmt).fetchone()
    if result:
        return dict(result)
    raise HTTPException(status_code=404, detail="Worker not found")

def convert_worker_to_dict(worker):
    return {
        "id": worker.id,
        "position": worker.position,
        "full_name": worker.full_name,
        "identifier": worker.identifier,
    }

def read_all_workers(db: Session):
    workers = db.query(Worker).all()
    
    # Convert each Worker instance to a dictionary
    return [convert_worker_to_dict(worker) for worker in workers]

def update_worker(db: Session, worker_id: int, updated_worker: dict):
    stmt = update(Worker).where(Worker.id == worker_id).values(updated_worker)
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Worker not found")
    db.commit()
    return {**updated_worker, "id": worker_id}

def delete_worker(db: Session, worker_id: int):
    stmt = Worker.__table__.delete().where(Worker.id == worker_id)
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Worker not found")
    db.commit()
    return {"message": "Worker deleted successfully"}

def create_assignment(db: Session, assignment: dict):
    try:
        result = db.execute(Assignment.__table__.insert().values(assignment))
        db.commit()
        return {"id": result.inserted_primary_key[0], **assignment}
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Assignment with this ID already exists",
        )

def read_assignment(db: Session, assignment_id: int):
    stmt = select(Assignment).where(Assignment.id == assignment_id)
    result = db.execute(stmt).fetchone()
    if result:
        return dict(result)
    raise HTTPException(status_code=404, detail="Assignment not found")

def update_assignment(db: Session, assignment_id: int, updated_assignment: dict):
    stmt = update(Assignment).where(Assignment.id == assignment_id).values(updated_assignment)
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Assignment not found")
    db.commit()
    return {**updated_assignment, "id": assignment_id}

def delete_assignment(db: Session, assignment_id: int):
    stmt = Assignment.__table__.delete().where(Assignment.id == assignment_id)
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Assignment not found")
    db.commit()
    return {"message": "Assignment deleted successfully"}



def read_projects_with_conditions(db: Session, name: str = None, deadline: datetime = None):
    stmt = select(Project).where(and_(Project.name == name, Project.deadline == deadline))
    results = db.execute(stmt).fetchall()
    return [row2dict(result) for result in results]


def read_projects_with_workers(db: Session):
    stmt = select(Project, Worker).join(Worker, Project.id == Assignment.project_id)
    results = db.execute(stmt).fetchall()
    return [{"project": row2dict(result[0]), "worker": row2dict(result[1])} for result in results]