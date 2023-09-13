from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/your_database_name"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# JWT Configuration
SECRET_KEY = "m.ghanbari717"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30