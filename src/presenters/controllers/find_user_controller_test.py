from faker import Faker

from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController

faker = Faker()


def test_handler():
    """Testing Handle Method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"user_id": faker.random_number()})

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_param["user_id"] == http_request.query["user_id"]

    # Testing Outputs
    assert response.status_code == 200
    assert response.body
