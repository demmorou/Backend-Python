from typing import Dict, List, Type
from src.domain.use_cases import FindPet as FindPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets


class FindPet(FindPetInterface):
    """Class to define use case find pet"""

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_id(self, pet_id: int) -> Dict[bool, Pets]:
        """Select pet by id
        :param - pet_id: id of the pet
        :return - Dictionary with proccess info
        """

        response = None
        input_is_valid = isinstance(pet_id, int)

        if input_is_valid:
            response = self.pet_repository.find_by_id(pet_id=pet_id)

        return {"Success": input_is_valid, "Data": response}

    def by_name(self, name: str) -> Dict[bool, Pets]:
        """Select pet by name
        :param - name: name of the pet
        :return - Dictionary with proccess info
        """

        response = None
        input_is_valid = isinstance(name, str)

        if input_is_valid:
            response = self.pet_repository.find_by_name(name=name)

        return {"Success": input_is_valid, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """select all pets by user id
        :param - user_id: id of the user
        :return - Dictionary with proccess info
        """

        data = None
        input_is_valid = isinstance(user_id, int)

        if input_is_valid:
            data = self.pet_repository.find_by_user_id(user_id=user_id)

        return {"Success": input_is_valid, "Data": data}
