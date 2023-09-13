from pydantic import BaseModel, validator, root_validator
from fastapi import Path
from handeling import JinjaExeption


class requestStudent(BaseModel):
    name: str
    family: str
    email: str
    phonenumber: str
    password: str
    class_id: int

    @root_validator(skip_on_failure=True)
    def validate_fields(cls, values):
        errors = {}

        if not values['name'].isalpha():
            errors['name'] = "Enter Just Characters For Name"

        if not values['family'].isalpha():
            errors['family'] = "Enter Just Characters For Family"

        if "@" not in values['email']:
            errors['email'] = "Email Must Have @"

        if len(values['phonenumber']) != 11:
            errors['phonenumber'] = "Number Must be 11 digits"
        elif values['phonenumber'][0:2] != "09":
            errors['phonenumber'] = "The Number Must Start with 09"
        elif not values['phonenumber'].isdigit():
            errors['phonenumber'] = "Input should only contain numeric digits"

        if values['class_id'] == 0:
            errors['class_id'] = "The Id Can Not Be 0"

        if errors:
            raise ValueError(errors)

        return values




class NewStudent(BaseModel):
    phonenumber: str


class read(BaseModel):
    name: str
    family: str
    email: str
    phonenumber: str
