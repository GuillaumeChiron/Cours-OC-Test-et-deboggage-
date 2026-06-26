import unittest
from calculate.operators import Operators

class TestOperatorAddition(unittest.TestCase):

    def test_should_make_addition(self):
        sut = Operators()
        operation = "5 + 10"
        expected_value = 15
        self.assertEqual(sut.addition(operation), expected_value)

    def test_should_make_multiple_addition(self):
        sut = Operators()
        operation = "10 + 3 + 7"
        expected_value = 20
        self.assertEqual(sut.addition(operation), expected_value)


if __name__ == "__main__":
    unittest.main()