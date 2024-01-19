from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from .auth_schemas import Token, UserLoginDTO
from .auth_service import AuthService


router_auth = APIRouter(
    prefix="/auth",
    tags=["security"]
)

@router_auth.post('/login', response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = UserLoginDTO(username=form_data.username, password=form_data.password)
    auth_service = AuthService(db='')
    auth_data = auth_service.login(user)

    return auth_data