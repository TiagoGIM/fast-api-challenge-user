from pydantic import BaseModel, ConfigDict,validator
import re
from ..enums.permissions import Roles
from typing import Optional ,TypeVar, Type

email_regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


class User(BaseModel):
    id: Optional[str]
    username: str
    password: str
    email:str
    role: Optional[Roles]
    model_config = ConfigDict(from_attributes=True)

    
    @validator('username')
    def validate_username(cls,value):
        if not re.match('^([a-z]|[0-9]|@)+$',value):
            raise ValueError('User name format invalid')
        return value
    
    @validator('email')
    def validate_email(cls,value):
        if not re.match(email_regex,value):
            raise ValueError('User email format invalid')
        return value

    
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
