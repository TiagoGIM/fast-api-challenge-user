from fastapi.exceptions import HTTPException
from fastapi import status

from .auth_schemas import Token, UserLoginDTO
from .auth_security import create_access_token, verify_password
from ..user.user_repository import UserRepository

class AuthService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    def login(self, user: UserLoginDTO) -> Token:
        user_found =  self.user_repository.get_by_username(user.username)

        if user_found is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User Not Found'
            )

        if not verify_password(user.password, user_found.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid credentials'
            )

        payload = {
            'sub': user.username,
        }

        access_token = create_access_token(data = payload)

        return {
            'access_token': access_token,
            'token_type': 'Bearer'
        }