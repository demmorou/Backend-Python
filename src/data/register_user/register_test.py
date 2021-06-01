from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser


faker = Faker()


def test_register():
    """Should be able register a new user"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.word()}

    response = register_user.execute(
        name=attributes["name"], password=attributes["password"]
    )

    # testing inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Should not be able register a new user"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.random_number(digits=3), "password": faker.word()}

    response = register_user.execute(
        name=attributes["name"], password=attributes["password"]
    )

    # testing inputs
    assert user_repo.insert_user_params == {}

    # testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
