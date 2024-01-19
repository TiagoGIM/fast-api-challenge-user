from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String ,Enum
import uuid
from ..user.user_schemas import User
from ..enums.permissions import Roles
from .connection import Base

class UserModel(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    username = Column(String, index=True, nullable=False, unique=True)
    email = Column(String, index=True, nullable=False , unique=True)
    password = Column(String, nullable=False)
    role = Column(Enum(Roles), default=Roles.REGULAR)

    def to_user(self):
        return User(username=self.username, email=self.email, id=str(self.id), role=self.role, password = self.password)
