import doctest


def repeat_sum(num:int) -> int:
    """ 
    Repeatedly sums up terms up to and including num
        * if num is even, sum up all even numbers
        * if num is odd, sum up all odd numbers
    
    >>> repeat_sum(10)
    30
    >>> repeat_sum(9)
    25
    >>> repeat_sum(20)
    110
    >>> repeat_sum(33)
    289
    >>> repeat_sum(-6)
    Traceback (most recent call last):
    ...
    AssertionError: num must be a non-negative int
    >>> repeat_sum("s")
    Traceback (most recent call last):
    ...
    AssertionError: num must be a non-negative int
    """
    
    assert type(num) == int and num >= 0, "num must be a non-negative int"
    
    if num % 2 == 0:
        start = 2
    else:
        start = 1
        
    total = 0
    
    for i in range(start, num + 1, 2):
        total = total + i
    
    return total

doctest.testmod()

print(repeat_sum(10))



