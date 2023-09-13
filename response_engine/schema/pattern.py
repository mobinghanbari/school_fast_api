from pydantic import BaseModel


class MyCustomResponse(BaseModel):
    message: str
    code: int
    data: dict
