from faker import Faker
from src.domain.models import Pets
from src.infra.entities import AnimalTypes

faker = Faker()


def mock_pet() -> Pets:
    """Mockging pets"""

    return Pets(
        id=faker.random_number(digits=5),
        name=faker.name(),
        specie=AnimalTypes.cat,
        age=faker.random_number(digits=1),
        user_id=faker.random_number(digits=5),
    )
