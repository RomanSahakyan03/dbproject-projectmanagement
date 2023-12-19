from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = "postgresql://postgres:root@localhost:5432/project_management"
engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base(metadata=MetaData())


Base.metadata.create_all(engine)