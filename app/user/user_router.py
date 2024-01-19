from ..user.user_service import UserService
from ..depends import get_db_session
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..user.user_schemas import UserCreateDTO

router_user = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router_user.post("/singin", status_code=201,)
def create_user(
    user : UserCreateDTO,
    db_session: Session = Depends(get_db_session)
                ):
    user_service = UserService(db_session)
    user_service.register(user)
    return {'message':'User created successfully', 'user' : user}
