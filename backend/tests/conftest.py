from app.services import get_db
from app.db import Base
from app.main import app
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import sys
import os

# Projenin kök dizinini (backend/) Python'un import yoluna ekliyoruz.
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))


# Test için hafızada (in-memory) bir SQLite veritabanı oluşturuyoruz.
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    # Sadece SQLite için gerekli bir ayar
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

# Her testten önce tabloları oluşturup, testten sonra temizliyoruz.


@pytest.fixture()
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


# Uygulamanın veritabanı bağımlılığını (get_db) test veritabanı ile
# değiştiriyoruz.
@pytest.fixture()
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    # Temizlik
    del app.dependency_overrides[get_db]
