import pytest
from faker import Faker

# Initialize the Faker object
fake = Faker()

@pytest.fixture
def fake_data():
    """Fixture that generates fake data for the tests."""
    return {
        'a': fake.random_int(min=1, max=100),    # Random integer for 'a'
        'b': fake.random_int(min=1, max=100),    # Random integer for 'b'
        'operation': fake.random_element(elements=('add', 'subtract', 'multiply', 'divide')),
        'expected': fake.random_int(min=1, max=100)
    }
