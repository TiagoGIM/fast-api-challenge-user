from fastapi import APIRouter
from ..user.user_schemas import UserCreateDTO

router_user = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router_user.post("/", status_code=201)
def create_user(user : UserCreateDTO):
    return {'message':'User created successfully', 'user' : user}
