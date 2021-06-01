from src.domain.test import mock_user
from src.domain.models import Users


class UserRepositorySpy:
    """Spy to User Repository"""

    def __init__(self):
        self.insert_user_params = {}
        self.find_user_by_id_params = {}
        self.find_user_by_name_params = {}

    def insert_user(self, name: str, password: str) -> Users:
        """Spy to allthe attributes"""

        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password

        return mock_user()

    def find_by_name(self, name: str) -> Users:
        """Spy to user attributes"""

        self.find_user_by_name_params["name"] = name

        return mock_user()

    def find_by_id(self, user_id: int) -> Users:
        """Spy to user attributes"""

        self.find_user_by_id_params["user_id"] = user_id

        return mock_user()
