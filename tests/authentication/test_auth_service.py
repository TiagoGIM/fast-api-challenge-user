# import pytest
# from app.authentication.auth_schemas import UserLoginDTO
# from app.authentication.auth_service import AuthService
# from app.authentication.auth_security import get_password_hash
# from fastapi.exceptions import HTTPException
# from app.user.user_schemas import User

# # @pytest.fixture
# # def auth_service(monkeypatch):
# #     mock_instance = AuthService('')
# #     # Substituir o retorno do método específico
# #     user = User(username='teste',password =get_password_hash('teste123'), email='')
# #     monkeypatch.setattr(mock_instance.user_repository, 'get_by_username', lambda username : user)
# #     return mock_instance 

# # def test_login_return_token(auth_service):
# #     hashed_password = get_password_hash('teste123')
# #     user_dto = UserLoginDTO(username="testuser", password=hashed_password)

# #     auth_data = auth_service.login(user_dto)

# #     assert 'access_token' in auth_data