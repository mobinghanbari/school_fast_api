from sqlalchemy.orm import Session
from database.models import Class
from handeling import JinjaExeption
import shutil


# Read
def get_class(db: Session, class_id):
    return db.query(Class).get(class_id)

def get_classes(db: Session,user_id):
    return db.query(Class).filter(Class.user_id == user_id).all()

# Create
def create_class(db: Session, name, description, photo):
    try:
        iname = photo.filename
        path = f"media/{iname}"
        with open(path, "wb") as f:
            shutil.copyfileobj(photo.file, f)

        # َCreate class object
        obj = Class(name=name, description=description, photo=path)
        db.add(obj)

        # Save in database
        db.commit()
        db.refresh(obj)

        return obj
    except Exception as e:
        raise JinjaExeption.internal_server_error(detail="Datbase is in fire")


# Update
def update_class_by_id(db: Session, class_id: int, description):
    try:
        the_class = db.query(Class).get(class_id)
        the_class.description = description
        db.commit()
        db.refresh(the_class)
        return db.query(Class).get(class_id)
    except Exception:
        JinjaExeption.internal_server_error(detail="Database Engine Is In Fire")


# Delete
def delete_by_id(db: Session, class_id: int):
    the_item = db.query(Class).get(class_id)
    if the_item:
        db.delete(the_item)
        db.commit()
        return {"message": "Item deleted successfully"}
    raise JinjaExeption.not_found(detail="Item Not Found")