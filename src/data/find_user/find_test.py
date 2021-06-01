from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser


faker = Faker()


def test_by_id():
    "Should be able test the method by_id()"

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attrbutes = {"id": faker.random_number(digits=3)}

    response = find_user.by_id(user_id=attrbutes["id"])

    # testing inputs
    assert user_repository.find_user_by_id_params["user_id"] == attrbutes["id"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_name():
    "Should be able test the method by_name()"

    user_repository = UserRepositorySpy()
    find_user = FindUser(user_repository)

    attrbutes = {"name": faker.name()}

    response = find_user.by_name(name=attrbutes["name"])

    # testing inputs
    assert user_repository.find_user_by_name_params["name"] == attrbutes["name"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]
