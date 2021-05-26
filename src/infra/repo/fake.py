# pylint: disable=E1101

from src.infra.config import DatabaseConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert_user(cls):
        """something"""
        with DatabaseConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Deusimar", password="123123")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
