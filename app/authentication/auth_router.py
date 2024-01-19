from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..user.user_schemas import User
from .auth_schemas import Token, UserLoginDTO
from .auth_service import AuthService
from .auth_security import create_access_token
from ..depends import get_current_user, get_db_session

router_auth = APIRouter(
    prefix="/auth",
    tags=["security"]
)

@router_auth.post('/login', response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db_session)
):
    user = UserLoginDTO(username=form_data.username, password=form_data.password)
    auth_service = AuthService(db_session)
    auth_data = auth_service.login(user)

    return auth_data

@router_auth.post('/refresh_token', response_model=Token)
def refresh_access_token(
    user: User = Depends(get_current_user),
):
    new_access_token = create_access_token(data={'sub': user.username})

    return {'access_token': new_access_token, 'token_type': 'bearer'}