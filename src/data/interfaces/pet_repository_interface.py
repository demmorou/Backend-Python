from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def create(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """abstract method"""

        raise Exception("Method not implemented")

    @abstractmethod
    def find_by_id(self, pet_id: int) -> Pets:
        """abstract method"""

        raise Exception("Method not implemented")

    @abstractmethod
    def find_by_name(self, name: str) -> Pets:
        """abstract method"""

        raise Exception("Method not implemented")

    @abstractmethod
    def find_by_user_id(self, user_id: int) -> List[Pets]:
        """abstract method"""

        raise Exception("Method not implemented")
