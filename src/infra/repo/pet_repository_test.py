from faker import Faker
from src.infra.config import DatabaseConnectionHandler
from src.infra.entities import AnimalTypes
from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DatabaseConnectionHandler()


def test_create_pet():
    """Should be able create a new pet"""

    name = faker.name()
    specie = AnimalTypes.cat
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    pet = pet_repository.create(name, specie, age, user_id)

    engine = db_connection_handler.get_engine()
    created_pet = engine.execute(f"SELECT * FROM pets WHERE id='{pet.id}';").fetchone()

    assert pet.id == created_pet.id
    assert pet.name == created_pet.name
    assert pet.specie == created_pet.specie
    assert pet.age == created_pet.age

    engine.execute(f"DELETE FROM pets WHERE id='{pet.id}';")
