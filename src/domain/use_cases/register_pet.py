from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import Pets


class RegisterPetInterface(ABC):
    """Interface to Register Pet Use Case"""

    @abstractclassmethod
    def registry(
        cls, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Register pet method"""

        raise Exception("Should implement mehtod: registry")
