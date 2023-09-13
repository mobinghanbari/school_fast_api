from pydantic import BaseModel
from pydantic import validator
from handeling import JinjaExeption

class requestClass(BaseModel):
    name: str
    description: str

    @validator("name")
    def validate_name(cls, v):
        if not v.isnumeric():
            return v
        raise JinjaExeption.bad_request(detail="Name should not contain raw numbers")

    @validator("description")
    def validate_description(cls, v):
        if not v.isnumeric():
            return v
        raise JinjaExeption.bad_request(detail="Description should not contain raw numbers")


class NewClass(BaseModel):
    description: str

    @validator("description")
    def validate_description(cls, v):
        if not v.isnumeric():
            return v
        raise JinjaExeption.bad_request(detail="Description should not contain raw numbers")

