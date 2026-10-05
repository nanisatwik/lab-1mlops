import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5

def test_fun2():
    assert calculator.fun2(5, 3) == 2

def test_fun3():
    assert calculator.fun3(2, 3) == 6

def test_fun4():
    assert calculator.fun4(2, 3) == 10

def test_fun5():
    assert calculator.fun5(10, 2) == 5

def test_negative():
    assert calculator.fun1(-2, -3) == -5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.fun5(5, 0)