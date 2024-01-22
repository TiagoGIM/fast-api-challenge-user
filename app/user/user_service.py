from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session , class_mapper
from sqlalchemy.exc import IntegrityError
from ..authentication.auth_security import get_password_hash
from ..db.models import UserModel
from ..user.user_repository import UserRepository
from ..user.user_schemas import UserCreateDTO, UserResponseDTO, UserUpdateDTO
from ..celery.celery_tasks import send_email
from uuid import UUID
class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(self, user_dto: UserCreateDTO):


        try:
            userToSave = UserModel(
            username = user_dto.username,
            email = user_dto.email,
            password = get_password_hash(user_dto.password)
        )
            user_created_with_sucess = self.user_repository.create(userToSave)
            user_created_with_sucess.email

            send_email(user_created_with_sucess.email).delay()
            
            return user_created_with_sucess
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User or email already exists'
            )
    
    def update(self, user : UserUpdateDTO, id:UUID) -> UserResponseDTO:
        try:
            user_found = self.user_repository.get_by_id(id)

            if not user_found:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='User not found'
                )
            
            user_to_update = self.merge_user(user, user_found)           
            user_response = self.user_repository.update(user_to_update)

            return user_response
        
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='UserUpdateDTO have some problem'
            )
          
    def get_user_by_user_name(self, username:str) ->  UserResponseDTO:
        try:
            found_user = self.user_repository.get_by_username(username)
            if found_user is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='User not found'
                )
            user_response = UserResponseDTO(**found_user.__dict__)
            return user_response
        except IntegrityError as e:
            raise HTTPException(
                status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail= e.orig.args if hasattr(e, 'orig') else f"{e}"
                )
        
    def all_users(self):
        return self.user_repository.get_all()
    
    def remove(self, user_id) -> bool:
        try:
            return self.user_repository.delete(user_id)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Coud not remove user'
            )
        
    def merge_user(self, user : UserUpdateDTO, usermodel : UserModel):
            
        mapper = class_mapper(UserModel)

        for column in mapper.columns:
            column_name = column.name
            if column_name in user.dict() and getattr(user, column_name) is not None:
                 setattr(usermodel,column_name,getattr(user, column_name))
               
        return usermodel