import pytest
from mypackage.calculator import add, subtract, multiply, divide, prime

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_prime():
    assert prime(5) == True






