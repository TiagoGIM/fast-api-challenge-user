from ..db.models import UserModel
from ..user.user_schemas import User
from sqlalchemy.orm import Session

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