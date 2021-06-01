from faker import Faker
from src.infra.test import PetRepositorySpy
from src.infra.entities import AnimalTypes
from .find import FindPet


faker = Faker()


def test_by_pet_id():
    """Should be able find a pet by id"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {
        "id": faker.random_number(digits=5),
        "name": faker.name(),
        "specie": AnimalTypes.cat,
        "age": faker.random_number(digits=1),
        "user_id": faker.random_number(digits=5),
    }

    data = find_pet.by_id(pet_id=attributes["id"])

    # testing inputs
    assert pet_repository.find_pet_by_id_params["pet_id"] == attributes["id"]

    # testing outputs
    assert data["Success"] is True
    assert data["Data"]


def test_find_by_invalid_id():
    """Should not be able find a pet with invalid input"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {
        "id": faker.name(),
        "name": faker.name(),
        "specie": AnimalTypes.cat,
        "age": faker.random_number(digits=1),
        "user_id": faker.random_number(digits=5),
    }

    data = find_pet.by_id(pet_id=attributes["id"])

    # testing outputs
    assert data["Success"] is False
    assert data["Data"] is None


def test_by_name():
    """Should be able find a pet by name"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {
        "id": faker.random_number(digits=5),
        "name": faker.name(),
        "specie": AnimalTypes.cat,
        "age": faker.random_number(digits=1),
        "user_id": faker.random_number(digits=5),
    }

    data = find_pet.by_name(name=attributes["name"])

    # testing inputs
    assert pet_repository.find_pet_by_name_params["name"] == attributes["name"]

    # testing outputs
    assert data["Success"] is True
    assert data["Data"]


def test_by_user_id():
    """Should be able find all pets by user id"""

    pet_repository = PetRepositorySpy()
    find_pet = FindPet(pet_repository)

    attributes = {
        "id": faker.random_number(digits=5),
        "name": faker.name(),
        "specie": AnimalTypes.cat,
        "age": faker.random_number(digits=1),
        "user_id": faker.random_number(digits=5),
    }

    data = find_pet.by_user_id(user_id=attributes["user_id"])

    # testing inputs
    assert pet_repository.find_pet_by_user_id_params["user_id"] == attributes["user_id"]

    # testing outputs
    assert data["Success"] is True
    assert isinstance(data["Data"], list)
