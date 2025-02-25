from faker import Faker
import pytest

# Example usage of Faker
fake = Faker()
print(fake.name())  # Print a fake name

# Example pytest function
def test_example():
    assert 1 + 1 == 2
