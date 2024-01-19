from ..db.models import UserModel
from ..user.user_schemas import User
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user : UserModel) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user.to_user()

    def get_by_username(self, username: str) -> User | None:
        try:
            found_user : UserModel = self.db.query(UserModel).filter(UserModel.username == username).first()
            return found_user.to_user() if found_user else None
        except Exception as e:
            raise Exception({"detail": e.orig.args if hasattr(e, 'orig') else f"{e}"})
            
    def get_by_id(self, id: UUID) -> UserModel:
        try:
            found_user : UserModel = self.db.query(UserModel).filter(UserModel.id == id).first()
            return  found_user
        except Exception as e:
            raise Exception({"detail": e.orig.args if hasattr(e, 'orig') else f"{e}"})
    
    def get_all(self) -> List[UserModel]:
        return self.db.query(UserModel).all()
    
    def update(self, user : UserModel) -> User:
        self.db.merge(user)
        self.db.commit()
        self.db.flush()
        return user.to_user()

    def delete(self, user_id : UUID):
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            self.db.flush()
            return True

        return False