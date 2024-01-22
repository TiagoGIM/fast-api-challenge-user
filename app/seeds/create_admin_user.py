from sqlalchemy.orm import Session

from ..enums.permissions import Roles
from ..user.user_service import UserService
from ..user.user_schemas import UserCreateDTO

def create_admin_user(db_session: Session):
    admin_data = {
        "username": "admin",
        "password": "admin1234",  # Lembre-se de usar um hash real para a senha
        "email": "admin@example.com",
        "role": Roles.ADMIN
    }

    admin_dto = UserCreateDTO(**admin_data)
    user_service = UserService(db_session)
    user_service.register(admin_dto)

if __name__ == "__main__":
    from app.db.connection import engine, Base, SessionLocal

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    create_admin_user(db)
    db.close()
