import doctest

def is_even(number: int)-> bool:
    """
    Returns true or false if a number is even or odd respectively

    >>> is_even(4)
    True
    >>> is_even(-5)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(5.5)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument
    >>> is_even("1")
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument
    """
    assert type(number) == int, "invalid argument"

    mod = number % 2

    return mod == 0

doctest.testmod()
