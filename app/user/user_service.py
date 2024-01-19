from ..user.user_repository import UserRepository
from ..user.user_schemas import User, UserCreateDTO


class UserService:
    def __init__(self):
        self.user_repository = UserRepository(db = '')

    def registre(self, user_dto: UserCreateDTO):
        user = User(**user_dto.dict())
        if len(user_dto.password) < 8:
            raise Exception("Password must be at least 8 characters long")

        return self.user_repository.create(user)
    