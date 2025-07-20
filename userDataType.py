from pydantic import BaseModel,AnyUrl,EmailStr


class Manjeet(BaseModel):
    id: str
    name: str
    age: int
