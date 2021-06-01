from typing import Type, Dict
from src.domain.use_cases import RegisterUserInterface
from src.domain.models import Users
from src.data.interfaces import UserRepositoryInterface as UserRepository


class RegisterUser(RegisterUserInterface):
    """Class to define use case: Register User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def execute(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user use case
        :param - name: person name
        :param - password: user password
        :return - Dictionary with informations of the process
        """

        user = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            user = self.user_repository.insert_user(name, password)

        return {"Success": validate_entry, "Data": user}
