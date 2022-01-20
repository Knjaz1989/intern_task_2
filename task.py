import pytest


def is_even(number):
    ''' Returns True if **number** is even or False if it is odd. '''
    if number % 2 == 0:
        return True
    return False


values = [
    (2, True),
    (1, False)
]

@pytest.mark.parametrize("number, result", values)
def test_is_even(number, result):

    assert is_even(number) == result
