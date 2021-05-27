from faker import Faker
from src.infra.config import DatabaseConnectionHandler
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DatabaseConnectionHandler()


def test_insert_user():
    """Should be able insert an user"""

    name = faker.name()
    password = faker.word()

    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)
    user = engine.execute(f"SELECT * FROM users WHERE id={new_user.id};").fetchone()

    engine.execute(f"DELETE FROM users WHERE id={new_user.id};")

    assert new_user.id == user.id
    assert new_user.name == user.name
    assert new_user.password == user.password


def test_find_by_name():
    """Should be able return an user by your name"""

    name = faker.name()
    password = faker.word()
    user = user_repository.insert_user(name=name, password=password)

    created_user = user_repository.find_by_name(name=name)

    assert user == created_user

    engine = db_connection_handler.get_engine()
    engine.execute(f"DELETE FROM users WHERE id='{user.id}';")


def test_find_by_id():
    """Should be able return an user by your id"""

    name = faker.name()
    password = faker.word()
    user = user_repository.insert_user(name=name, password=password)

    created_user = user_repository.find_by_id(user_id=user.id)

    assert user == created_user

    engine = db_connection_handler.get_engine()
    engine.execute(f"DELETE FROM users WHERE id='{user.id}';")
