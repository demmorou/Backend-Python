from typing import Dict, Type
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Users


class FindUser(FindUserInterface):
    """Class to define use case find user"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, Users]:
        """Select user by id
        :param - user_id: id of th user
        :return - Dictionary with proccess info
        """

        response = None
        input_is_valid = isinstance(user_id, int)

        if input_is_valid:
            response = self.user_repository.find_by_id(user_id=user_id)

        return {"Success": input_is_valid, "Data": response}

    def by_name(self, name: str) -> Dict[bool, Users]:
        """Select user by name
        :param - name: name of th user
        :return - Dictionary with proccess info
        """

        response = None
        input_is_valid = isinstance(name, str)

        if input_is_valid:
            response = self.user_repository.find_by_name(name=name)

        return {"Success": input_is_valid, "Data": response}
