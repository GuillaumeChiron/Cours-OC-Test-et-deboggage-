from calculate.operators import Operators

def test_should_make_multiple_addtions():
    sut = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected_value = 59.2
    assert sut.addition(operation=operation) == expected_value


def test_should_make_multiplication():
    sut = Operators()
    operation = "5 * 2 * 3"
    expected_value = 30
    assert sut.multiplication(operation=operation) == expected_value