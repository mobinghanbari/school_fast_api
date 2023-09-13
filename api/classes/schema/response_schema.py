from pydantic import BaseModel



class responseClass(BaseModel):
    name: str
    description: str