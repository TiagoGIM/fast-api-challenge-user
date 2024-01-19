from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..authentication.auth_security import get_password_hash
from ..db.models import UserModel
from ..user.user_repository import UserRepository
from ..user.user_schemas import UserCreateDTO


class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(self, user_dto: UserCreateDTO):

        userToSave = UserModel(
            username = user_dto.username,
            email = user_dto.email,
            password = get_password_hash(user_dto.password)
        )
        try:
            self.user_repository.create(userToSave)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )
    