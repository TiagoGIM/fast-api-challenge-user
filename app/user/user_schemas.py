from pydantic import BaseModel, ConfigDict
from ..enums.permissions import Roles
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    username: str
    password: str
    email:str
    role: Optional[Roles]
    model_config = ConfigDict(from_attributes=True)

    
class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str

class UserResponseDTO(BaseModel):
    id: str
    username: str
    email: str
    role: Roles