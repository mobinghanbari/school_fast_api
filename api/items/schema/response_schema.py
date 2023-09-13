from pydantic import BaseModel


class responseStudent(BaseModel):
    name: str
    family: str
    phonenumber: str