from faker import Faker
from src.infra.config import DatabaseConnectionHandler
from src.infra.entities import AnimalTypes, Pets
from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DatabaseConnectionHandler()


def test_create_pet():
    """Should be able create a new pet"""

    name = faker.name()
    specie = AnimalTypes("cat")
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


def test_find_by_id():
    """Should be able return by your id"""

    name = faker.name()
    specie = AnimalTypes("cat")
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    pet = pet_repository.create(name, specie, age, user_id)

    engine = db_connection_handler.get_engine()
    created_pet = pet_repository.find_by_id(pet_id=pet.id)

    assert pet.id == created_pet.id
    assert pet.name == created_pet.name
    assert pet.specie == created_pet.specie
    assert pet.age == created_pet.age

    engine.execute(f"DELETE FROM pets WHERE id='{pet.id}';")


def test_find_by_name():
    """Should be able return by your name"""

    name = faker.name()
    specie = AnimalTypes("cat")
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    pet = pet_repository.create(name, specie, age, user_id)

    engine = db_connection_handler.get_engine()
    created_pet = pet_repository.find_by_name(name=name)

    assert pet.id == created_pet.id
    assert pet.name == created_pet.name
    assert pet.specie == created_pet.specie
    assert pet.age == created_pet.age

    engine.execute(f"DELETE FROM pets WHERE id='{pet.id}';")


def test_find_by_user_id():
    """Should be able return by your name"""

    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "dog"
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=5)

    specie_mock = AnimalTypes("dog")

    data = Pets(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    engine = db_connection_handler.get_engine()

    engine.execute(
        "INSERT INTO pets (id, name, specie, age, user_id) VALUES ('{}', '{}', '{}', '{}', '{}');".format(
            pet_id, name, specie, age, user_id
        )
    )

    pets = pet_repository.find_by_user_id(user_id=user_id)

    assert data in pets

    engine.execute(f"DELETE FROM pets WHERE id='{pet_id}';")
