from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

import os

DB_USER = os.getenv("POSTGRES_USER", "appuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "apppass")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "appdb")

DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DATABASE_URL = os.getenv(
#     "DATABASE_URL",
#     "postgresql+psycopg://appuser:apppass@db:5432/appdb")

# DATABASE_URL = f"postgresql+psycopg://{os.getenv('POSTGRES_USER','appuser')}:{os.getenv('POSTGRES_PASSWORD','apppass')}@{os.getenv('POSTGRES_HOST','db')}:{os.getenv('POSTGRES_PORT','5432')}/{os.getenv('POSTGRES_DB','appdb')}"

class Base(DeclarativeBase):
    pass

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
