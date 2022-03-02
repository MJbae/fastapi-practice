import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "mysql123456")
    user, db_name = "root", "allocation"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


SQLALCHEMY_DATABASE_URL = get_postgres_uri()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
