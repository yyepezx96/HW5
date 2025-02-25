import pytest
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add():
    add_command = AddCommand()
    result = add_command.execute(2, 3)
    assert result == 5

def test_subtract():
    subtract_command = SubtractCommand()
    result = subtract_command.execute(5, 3)
    assert result == 2

def test_multiply():
    multiply_command = MultiplyCommand()
    result = multiply_command.execute(2, 3)
    assert result == 6

def test_divide():
    divide_command = DivideCommand()
    result = divide_command.execute(6, 3)
    assert result == 2

def test_divide_by_zero():
    divide_command = DivideCommand()
    with pytest.raises(ValueError):
        divide_command.execute(6, 0)

