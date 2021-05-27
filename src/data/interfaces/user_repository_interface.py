from abc import ABC, abstractmethod
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface to User Repository"""

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """abstract method"""

        raise Exception("Method not implemented")

    @abstractmethod
    def find_by_id(self, user_id: int) -> Users:
        """abstract method"""

        raise Exception("Method not implemented")

    @abstractmethod
    def find_by_name(self, name: str) -> Users:
        """abstract method"""

        raise Exception("Method not implemented")
