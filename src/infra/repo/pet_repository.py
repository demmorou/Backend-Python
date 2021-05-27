# pylint: disable=E1101

from typing import List
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

    @classmethod
    def find_by_id(cls, pet_id: int) -> Pets:
        """Return a pet by you id
        :param - pet_id: Pet's id
        return: Returns a pet
        """

        with DatabaseConnectionHandler() as db_connection:
            try:
                pet = db_connection.session.query(PetsModel).filter_by(id=pet_id).one()

                return PetsModel(
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

    @classmethod
    def find_by_name(cls, name: str) -> Pets:
        """Return a pet by you name
        :param - name: Pet's name
        return: Returns a pet
        """

        with DatabaseConnectionHandler() as db_connection:
            try:
                pet = db_connection.session.query(PetsModel).filter_by(name=name).one()

                return PetsModel(
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

    @classmethod
    def find_by_user_id(cls, user_id: int) -> List[Pets]:
        """Return a list of pets by user_id
        :param - user_id: Pet's user_id
        return: Returns a list with pets selecteds
        """

        with DatabaseConnectionHandler() as db_connection:
            try:
                pets = (
                    db_connection.session.query(PetsModel)
                    .filter_by(user_id=user_id)
                    .all()
                )

                return pets
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
