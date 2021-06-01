from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPet(ABC):
    """Abstract to find pet use case"""

    @abstractclassmethod
    def by_id(cls, pet_id: int) -> Dict[bool, Pets]:
        """Abstract method"""

        raise Exception("This method should be implemented")

    @abstractclassmethod
    def by_name(cls, name: str) -> Dict[bool, Pets]:
        """Abstract method"""

        raise Exception("This method should be implemented")

    @abstractclassmethod
    def by_user_id(cls, user_id: int) -> Dict[bool, List[Pets]]:
        """Abstract method"""

        raise Exception("This method should be implemented")
