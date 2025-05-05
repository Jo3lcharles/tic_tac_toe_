import doctest

def get_larger(num_1: float, num_2: float) -> float: 
    """return the larger of the two numbers.
    Precondition: num_1 float
                  num_2 float
    
    >>> get_larger(1.0, 2.0)
    2.0
    >>> get_larger(3.5, 1.5)
    3.5
    >>> get_larger(2, 2.2)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument: num_1 does not have the right type!
    >>> get_larger('1', 3.2)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument: num_1 does not have the right type!
    """

    assert type(num_1) == float, "invalid argument: num_1 does not have the right type!"
    assert type(num_2) == float, "invalid argument: num_2 does not have the right type!"
    
    return max(num_1, num_2)

get_larger('3', 1)
# doctest.testmod()