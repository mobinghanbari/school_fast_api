from pydantic import BaseModel, validator


class Login(BaseModel):
    phone: str
    password: str
