from ..user.user_schemas import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def create(self, user ) -> User:

        return user