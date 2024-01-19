from pydantic import BaseModel, ConfigDict
from ..enums.permissions import Roles
from typing import Optional ,TypeVar, Type

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

class UserUpdateDTO(BaseModel):
    id: Optional[str]
    username: Optional[str]
    email: Optional[str]

class Message(BaseModel):
    message: str

TModel = TypeVar('TModel')


def map_dto_to_model(dto: BaseModel, model_type: Type[TModel]) -> TModel:
    model_data = {key: value for key, value in dto.dict(exclude_unset=True).items() if value is not None}
     
    return model_type(**model_data)
