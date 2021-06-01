from typing import List
from src.domain.test import mock_pet
from src.domain.models import Pets


class PetRepositorySpy:
    """Spy to Pet Repository"""

    def __init__(self):
        self.insert_pet_params = {}
        self.find_pet_by_id_params = {}
        self.find_pet_by_name_params = {}
        self.find_pet_by_user_id_params = {}

    def create(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Spy to all the attributes"""

        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id

        return mock_pet()

    def find_by_id(self, pet_id: int) -> Pets:
        """Spy to all the attributes"""

        self.find_pet_by_id_params["pet_id"] = pet_id

        return mock_pet()

    def find_by_name(self, name: str) -> Pets:
        """Spy to all the attributes"""

        self.find_pet_by_name_params["name"] = name

        return mock_pet()

    def find_by_user_id(self, user_id: int) -> List[Pets]:
        """Spy to all the attributes"""

        self.find_pet_by_user_id_params["user_id"] = user_id

        return [mock_pet()]
