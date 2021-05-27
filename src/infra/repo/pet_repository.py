# pylint: disable=E1101

from src.domain.models import Pets
from src.infra.config import DatabaseConnectionHandler
from src.infra.entities import Pets as PetsModel


class PetRepository:
    """Class to manage Pet Repository"""

    @classmethod
    def create(cls, name: str, specie: str, age: int, user_id: int) -> Pets:
        """
        Create a new pet
        :param - name:
        :param - specie:
        :param - age:
        :param - user_id:
        :return - tuple with new pet
        """

        with DatabaseConnectionHandler() as db_connection:
            try:
                pet = PetsModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(pet)
                db_connection.session.commit()

                return Pets(
                    id=pet.id,
                    name=pet.name,
                    specie=pet.specie.value,
                    age=pet.age,
                    user_id=pet.user_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
