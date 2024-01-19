from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from fastapi import status
from decouple import config
from jose import jwt ,JWTError
from passlib.context import CryptContext

from .auth_schemas import Token, UserLoginDTO
from .auth_security import create_access_token, verify_password
from ..user.user_repository import UserRepository


SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 60
pwd_context = CryptContext(schemes=['sha256_crypt'])

class AuthService:
    def __init__(self, db: Session):
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
    
    def get_user_by_token(self, access_token: str ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = data.get("sub")
            if username is None:
               raise credentials_exception 
        except JWTError:
            raise credentials_exception
        
        user_found = self.user_repository.get_by_username(username)

        if user_found is None:
            raise credentials_exception
        
        return user_found