import doctest

def is_prime(num: int)-> bool:
    """
    determine whether a number is prime 
    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    >>> is_prime(23)
    True
    """

    assert type(num) == int and num>0, "num must be postive int"

    if num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True


def count_primes(start: int, stop: int)-> int:
    """
    Counts the total of prime numbers in the range [start, stop]

    >>> count_primes(3, 10)
    3
    >>> count_primes(2, 12)
    5
    >>> count_primes(1, 100)
    25
    """
    assert type(start) == int and start > 0, " start must be a positive int"
    assert type(stop) == int and stop > 0, " stop must be a positive int"

    counter = 0

    for num in range (start, stop + 1):
        if is_prime(num):
            counter += 1

    return counter


doctest.testmod()