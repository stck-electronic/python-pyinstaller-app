
import sys
sys.path.append("../sources")
import calc


def test_add_integers():
    """
    Test that the addition of two integers returns the correct total
    """
    result = calc.add2(1, 2)
    assert result == 3

def test_add_2floats():
    """
    Test that the addition of two floats returns the correct result
    """
    result = calc.add2('10.5', '12.0')
    assert result == 22.5

def test_add_floats():
    """
    Test that the addition of two floats returns the correct result
    """
    result = calc.add2('10.5', 2)
    assert result == 12.5

def test_add_strings():
    """
    Test the addition of two strings returns the two strings as one
    concatenated string
    """
    result = calc.add2('abc', 'def')
    assert result == 'abcdef'

def test_add_string_and_integer():
    """
    Test the addition of a string and an integer returns them as one
    concatenated string (in which the integer is converted to a string)
    """
    result = calc.add2('abc', 3)
    assert result == 'abc3'

def test_add_string_and_number():
    """
    Test the addition of a string and a float returns them as one
    concatenated string (in which the float is converted to a string)
    """
    result = calc.add2('abc', '5.5')
    assert result == 'abc5.5'

