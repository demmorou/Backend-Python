from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterPetController
from src.data.register_pet import RegisterPet
from src.infra.repo.pet_repository import PetRepository
from src.infra.repo.user_repository import UserRepository


def register_pet_compose() -> RouteInterface:
    """Composing register user route
    :param - None
    :return - Object with registered user
    """
    pets_repository = PetRepository()
    users_repository = UserRepository()
    use_case = RegisterPet(pets_repository, users_repository)
    register_pet_route = RegisterPetController(use_case)

    return register_pet_route
