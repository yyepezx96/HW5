import pytest
from calculator import Calculator

def test_calculator_operations(fake_data):
    for data in fake_data:
        a = data['a']
        b = data['b']
        operation = data['operation']
        expected = data['expected']

        calc = Calculator()

        if operation == 'add':
            result = calc.add(a

