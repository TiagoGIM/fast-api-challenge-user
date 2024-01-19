from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,status
from fastapi.exceptions import HTTPException

from .enums.permissions import Roles
from .user.user_schemas import User
from .authentication.auth_service import AuthService
from .db.connection import Session
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/auth/login')

def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

async def get_current_user(
        token = Depends(oauth2_scheme),
        db_session:Session=Depends(get_db_session)
    ):
    auth_service = AuthService(db_session)

    user = auth_service.get_user_by_token(token)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

class PermissionChecker:

    def __init__(self, required_permissions: Roles = Roles.REGULAR) -> None:
        self.required_permissions = required_permissions

    def __call__(self, user: User = Depends(get_current_user)) -> User:
        print(user.role , self.required_permissions)
        if not user.role == self.required_permissions:
            
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Permissions'
                )
        return user