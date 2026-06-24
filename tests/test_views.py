from calculate.view import View

def test_user_input():
    sut = View()
    expected_value = "hello"
    assert sut.get_user_input("Saisir hello") == expected_value
    