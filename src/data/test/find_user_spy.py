from typing import Dict
from src.domain.models import Users
from src.domain.test import mock_user


class FindUserSpy:
    """Class to define use case: Select User"""

    def __init__(self, user_repository: any) -> None:
        self.user_repository = user_repository
        self.by_id_param = {}
        self.by_name_param = {}

    def by_id(self, user_id: int) -> Dict[bool, Users]:
        """Select User By Id"""

        self.by_id_param["user_id"] = user_id

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = mock_user()

        return {"Success": validate_entry, "Data": response}

    def by_name(self, user_name: str) -> Dict[bool, Users]:
        """Select User By Id"""

        self.by_name_param["user_name"] = user_name

        response = None

        validate_entry = isinstance(user_name, str)

        if validate_entry:
            response = mock_user()

        return {"Success": validate_entry, "Data": response}
