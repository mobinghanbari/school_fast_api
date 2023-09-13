from fastapi import APIRouter, status, Depends, BackgroundTasks, Request
from .endpoint import *
from database import get_db
from .schema import *
from authentications import has_access
from fastapi import UploadFile, File
from fastapi.staticfiles import StaticFiles
from .log_process import create_log
from response_engine.schema import MyCustomResponse



class_item_router = APIRouter(tags=["Class"])
class_item_router.mount("/media", StaticFiles(directory="media"), name="media")


# Get all classes
@class_item_router.get("/classes", status_code=status.HTTP_200_OK)
def read_items(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user=Depends(has_access)):
    background_tasks.add_task(create_log, f"Received request: Method='POST', URL='{request.method}://{request.client.host}:{request.client.port}{request.url}', Client Host='{request.client.host}'")
    info =  get_class(db, class_id=current_user.class_id)
    return MyCustomResponse(message="These are your class data", code=status.HTTP_200_OK, data={"id":info.id, "name":info.name, "description":info.description, "photo":info.photo, "created_at":info.created_at, "updated_at":info.updated_at})

# Add new class
@class_item_router.post("/classes", response_model=None, status_code=status.HTTP_200_OK)
def add_new_class(request: Request, background_tasks: BackgroundTasks, name:str, description:str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    alowed_formats = ["jpg", "jpeg"]
    file_type = file.filename.split(".")[-1].lower()
    if file_type not in alowed_formats:
        background_tasks.add_task(create_log, f"Received request: Method='{request.method}', URL='{request.url}', Client Host='{request.client.host}")
        raise JinjaExeption.bad_request(detail="Invalid file format. Only JPG and JPEG formats are allowed.")

    background_tasks.add_task(create_log, f"Received request: Method='{request.method}', URL='{request.url}', Client Host='{request.client.host}")
    info = create_class(db, name=name, description=description, photo=file)
    return MyCustomResponse(message="Class Created Successfully", code=status.HTTP_201_CREATED, data={"id":info.id, "name":info.name, "description":info.description, "photo":info.photo, "created_at":info.created_at, "updated_at":info.updated_at})

# Update class by id and description
@class_item_router.put("/classes", response_model=None, status_code=status.HTTP_200_OK)
def update_item(request: Request, background_tasks: BackgroundTasks, item: NewClass, db: Session = Depends(get_db), current_user=Depends(has_access)):
    background_tasks.add_task(create_log, f"Received request: Method='{request.method}', URL='{request.url}', Client Host='{request.client.host}")
    info = update_class_by_id(db, class_id=current_user.class_id, description=item.description)
    return MyCustomResponse(message="Class Updated Successfully", code=status.HTTP_200_OK, data={"id":info.id, "name":info.name, "description":info.description, "photo":info.photo, "created_at":info.created_at, "updated_at":info.updated_at})


# Remove class by id
@class_item_router.delete("/classes", status_code=status.HTTP_200_OK)
def delete_item(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user=Depends(has_access)):
    background_tasks.add_task(create_log, f"Received request: Method='{request.method}', URL='{request.url}', Client Host='{request.client.host}")
    info = delete_by_id(db, class_id=current_user.class_id)
    return MyCustomResponse(message="Class Removed Successfully", code=status.HTTP_200_OK, data={})