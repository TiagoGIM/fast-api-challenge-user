from ..db.models import UserModel
from ..user.user_schemas import User
from sqlalchemy.orm import Session
from typing import List

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user : UserModel) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user.to_user()

    def get_by_username(self, username: str) -> User | None:
        found_user = self.db.query(UserModel).filter(UserModel.username == username).first()

        return found_user if found_user else None
    
    def get_all(self) -> List[UserModel]:
        return self.db.query(UserModel).all()
    
    def update(self, user : UserModel) -> User:
        self.db.merge(user)
        self.db.commit()
        self.db.flush()
        return user.to_user()

    def delete(self, user_id):
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            self.db.flush()
            return True

        return False