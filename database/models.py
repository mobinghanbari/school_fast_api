from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, VARCHAR, Text, BLOB
from sqlalchemy.orm import relationship
from datetime import datetime
from .connection import Base



class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    description = Column(Text)
    photo = Column("photo", VARCHAR(150))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    student = relationship("Student", backref="class")




class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    family = Column(VARCHAR(255))
    email = Column(VARCHAR(100))
    phonenumber = Column(VARCHAR(11))
    class_id = Column(Integer, ForeignKey(Class.id))
    password = Column(VARCHAR(250))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    email = Column(VARCHAR(255))
    phone = Column(VARCHAR(11))
    password = Column(VARCHAR(255))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())