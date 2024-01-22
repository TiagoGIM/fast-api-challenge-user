from fastapi import APIRouter, Depends, status, Response,Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from ..enums.permissions import Roles
from ..user.user_service import UserService
from ..depends import PermissionChecker, get_current_user, get_db_session
from ..user.user_schemas import  UserCreateDTO, UserResponseDTO, UserUpdateDTO, Message, User

router_user = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router_user.post("/singin", status_code=status.HTTP_201_CREATED, response_model = Message)
async def create_user(
    user : UserCreateDTO,
    db_session: Session = Depends(get_db_session),
    ):
    user_service = UserService(db_session)
    user_service.register(user)
    return Message(message ='User created successfully')
        

@router_user.get("/{username}", response_model=UserResponseDTO)
async def get_user_by_name(
    username: str,
    db_session: Session = Depends(get_db_session),
    current_user : User = Depends(get_current_user)
    ):
    user_service = UserService(db_session)

    try:
        return user_service.get_user_by_user_name(username)
    except Exception :
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='User not found')

        
@router_user.put("/update/{id}", response_model=UserResponseDTO)
async def update_user(
    id : str,
    user : UserUpdateDTO,
    db_session: Session = Depends(get_db_session),
    current_user : User = Depends(get_current_user)
    ):

    user_service = UserService(db_session)
    user_service.update(user, id)
    return  user_service.update(user, id)
    
    
@router_user.delete("/remove/{id}" , response_model=str)
async def remove_user(
    id: str,
    response : Response,
    db_session: Session = Depends(get_db_session),
    user : User = Depends(PermissionChecker(required_permissions=Roles.ADMIN))
    ) -> str :
    user_service = UserService(db_session)

    if (not user_service.remove(id)):
        response.status_code = status.HTTP_204_NO_CONTENT
        return  "user not found" 
    
    return  "user deleted with success"
