# pylint: disable=E1101

from src.domain.models import Users
from src.infra.config import DatabaseConnectionHandler
from src.infra.entities import Users as UsersModels


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """insert data in user entity
        :param - name: user name
        :      - password: user password
        :return - tuple with new user inserted
        """

        with DatabaseConnectionHandler() as db_connection:
            try:
                new_user = UsersModels(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
