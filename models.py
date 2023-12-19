from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    deadline = Column(Date, default=None)
    workload = Column(Float, default=0.0)
    code = Column(Integer, index=True)

    assignments = relationship("Assignment", back_populates="project")

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    issue_date = Column(Date, default=None)
    full_completion_date = Column(Date, default=None)
    actual_completion_date = Column(Date, default=None)
    workload = Column(Float, default=0.0)
    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"), index=True)

    project = relationship("Project", back_populates="assignments")
    worker = relationship("Worker", back_populates="assignments")

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    position = Column(String)
    full_name = Column(String, index=True)
    identifier = Column(String)

    assignments = relationship("Assignment", back_populates="worker")


# Project_Pydantic = sqlalchemy_to_pydantic(Project, exclude=['assignments'])
# Assignment_Pydantic = sqlalchemy_to_pydantic(Assignment)
# Worker_Pydantic = sqlalchemy_to_pydantic(Worker, exclude=['assignments'])