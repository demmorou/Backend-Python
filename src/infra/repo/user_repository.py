# pylint: disable=E1101

from src.domain.models import Users
from src.data.interfaces import UserRepositoryInterface
from src.infra.config import DatabaseConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository(UserRepositoryInterface):
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
                new_user = UsersModel(name=name, password=password)
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

    @classmethod
    def find_by_name(cls, name: str) -> Users:
        """Find an User by your name
        :param - name: User's name
        :return - Returns an user
        """

        with DatabaseConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(UsersModel).filter_by(name=name).one()
                )
                return user
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def find_by_id(cls, user_id: str) -> Users:
        """Find an User by your id
        :param - user_id: User's id
        :return - Returns an user
        """

        with DatabaseConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(UsersModel).filter_by(id=user_id).one()
                )
                return user
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
