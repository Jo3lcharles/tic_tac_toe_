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
        #else:
            #return True
    return True

print(is_prime(17))
        
    