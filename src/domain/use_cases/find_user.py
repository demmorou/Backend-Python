from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import Users


class FindUser(ABC):
    """Interface to find user user case"""

    @abstractclassmethod
    def by_id(cls, user_id: int) -> Dict[bool, Users]:
        """Abstract method"""

        raise Exception("This method should be implemented")

    @abstractclassmethod
    def by_name(cls, name: str) -> Dict[bool, Users]:
        """Abstract method"""

        raise Exception("This method should be implemented")
