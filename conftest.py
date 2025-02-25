import pytest
from faker import Faker

@pytest.fixture
def fake_data():
    fake = Faker()
    data = []
    for _ in range(10):  # Generate 10 records
        record = {
            'a': fake.random_number(),
            'b': fake.random_number(),
            'operation': fake.random_element(['add', 'subtract', 'multiply', 'divide']),
            'expected': fake.random_number()  # This will be a placeholder for the expected result
        }
        data.append(record)
    return data


