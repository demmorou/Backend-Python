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

    assert new_user.id == user.id
    assert new_user.name == user.name
    assert new_user.password == user.password
