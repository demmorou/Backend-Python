from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUserInterface(ABC):
    """Interface to register an user"""

    @abstractmethod
    def execute(self, name: str, password: str) -> Dict[bool, Users]:
        """abstract method"""

        raise Exception("Method not implemented")
