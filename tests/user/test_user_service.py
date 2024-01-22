import pytest
from app.user.user_schemas import UserCreateDTO

from app.user.user_service import UserService 

@pytest.fixture
def user_service():
    return UserService()



def test_create_user(user_service):
    user_dto = UserCreateDTO(username="testuser", password="testpassword", email="smeemai@email.com")
    created_user = user_service.registre(user_dto)
    assert created_user.username == "testuser"

def test_fail_create_user(user_service):
    user_dto = UserCreateDTO(username="testuser", password="", email="smeemai@email.com")
    with pytest.raises(Exception):
        user_service.register(user_dto)

