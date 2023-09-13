from sqlalchemy.orm import Session
from database.models import Student
from jwt import create_access_token
from handeling import JinjaExeption
from .hashing import hash_maker, verify_password


# Read
def get_student(db: Session, user_id):
    return db.query(Student).get(user_id)


def login(db: Session, phone:str, password:str):
    the_user = db.query(Student).filter(Student.phonenumber == phone).first()
    if not the_user:
        raise JinjaExeption.not_found(detail="Invalid Data")
    if not verify_password(password, the_user.password):
        raise JinjaExeption.not_found(detail="Incorrect Password")

    access_token = create_access_token(data={"sub": the_user.email})
    # return {"access_token": access_token, "token_type": "bearer"}
    return access_token

def get_students(db: Session, user_id: int):
    return db.query(Student).filter(Student.id == user_id).first()

# Create
def create_stuent(db: Session, name:str, family:str, email:str, phonenumber:str, class_id:int, password:str):
    pass_hash = hash_maker(password)
    stu = Student(name=name, family=family, email=email, phonenumber=phonenumber, class_id=class_id, password=pass_hash)
    db.add(stu)
    db.commit()
    db.refresh(stu)
    return stu


# Update
def update_student_by_id(db: Session, user_id: int, phonenumber:str):
    try:
        the_stu = db.query(Student).get(user_id)
        the_stu.phonenumber = phonenumber
        db.commit()
        db.refresh(the_stu)
        return db.query(Student).get(user_id)
    except Exception:
        JinjaExeption.internal_server_error(detail="Database Engine Is In Fire")


# Delete
def delete_by_id(db: Session, user_id: int):
    the_item = db.query(Student).get(user_id)
    if the_item:
        db.delete(the_item)
        db.commit()
        return {"message": "Item deleted successfully"}
    raise JinjaExeption.not_found(detail="Item not found")