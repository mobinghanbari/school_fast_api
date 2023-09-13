from fastapi import APIRouter, status, Request
from authentications.schema.request import Login
from database.connection import get_db
from .endpoint import *
from .schema import *
from .endpoint import login
from fastapi import  Depends, BackgroundTasks
from authentications import has_access
from .log_process import create_log
from response_engine.schema import MyCustomResponse


# routes

item_router = APIRouter(tags=['Student'])

# Add new student
@item_router.post("/api/items", response_model=None, status_code=status.HTTP_201_CREATED)
def create_item(request: Request, background_tasks: BackgroundTasks, item: requestStudent, db: Session = Depends(get_db)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    info =  create_stuent(db, name=item.name, family=item.family, email=item.email, phonenumber=item.phonenumber, class_id=item.class_id, password=item.password)
    return MyCustomResponse(message="Item Created", code=status.HTTP_201_CREATED, data={"id":info.id, "name":info.name, "family":info.family, "email":info.email, "phonenumber":info.phonenumber, "created_at":info.created_at, "updated_at":info.updated_at})

@item_router.post("/api/items/login")
def do_login(request: Request, background_tasks: BackgroundTasks, user: Login, db: Session = Depends(get_db)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")

    info = login(db, phone=user.phone, password=user.password)
    return MyCustomResponse(message="Welcome", code=status.HTTP_200_OK, data= {"access_token": info, "token_type": "bearer"})



# Get all stuednts
@item_router.get("/api/items", status_code=status.HTTP_200_OK)
def read_items(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db),  current_user=Depends(has_access)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    info = get_students(db, user_id=current_user.id)
    return MyCustomResponse(message="These are your data", code=status.HTTP_200_OK, data={"id":info.id, "name":info.name, "family":info.family, "email":info.email, "phonenumber":info.phonenumber, "created_at":info.created_at, "updated_at":info.updated_at})


# Update item by id
@item_router.put("/api/items", response_model=None, status_code=status.HTTP_200_OK)
def update_item(request: Request, background_tasks: BackgroundTasks, item: NewStudent, db: Session = Depends(get_db), current_user=Depends(has_access)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    info = update_student_by_id(db, current_user.id, phonenumber=item.phonenumber)
    return MyCustomResponse(message="Student edited successfully", code=status.HTTP_200_OK, data={"id":info.id, "name":info.name, "family":info.family, "email":info.email, "phonenumber":info.phonenumber, "created_at":info.created_at, "updated_at":info.updated_at})



# Remove item by id
@item_router.delete("/api/items", status_code=status.HTTP_200_OK)
def delete_item(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user=Depends(has_access)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    info = delete_by_id(db, user_id=current_user.id)
    return MyCustomResponse(message="Student deleted successfully", code=status.HTTP_200_OK, data={})
