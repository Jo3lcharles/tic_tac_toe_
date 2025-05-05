import doctest

def need_to_buy_ticket(age: float, height: float) -> bool:
    """
    Return whether a child should a ticket to enter the park

    >>> need_to_buy_ticket(2, 188)
    True
    >>> need_to_buy_ticket(2, 100)
    False
    >>> need_to_buy_ticket(0, 0)
    Traceback (most recent call last):
    ...
    AssertionError: age should be above 0
    >>> need_to_buy_ticket(-3, 33)
    Traceback (most recent call last):
    ...
    AssertionError: age should be above 0
    
    """

    assert age > 0 ,"age should be above 0"
    assert height > 0, "height should be above 0"

    # you can add any line of code between this line and the line with return
    x = age > 6
    y = height > 120

    result = ((x or y) and y) or x
    # show result
    return result # You should modify this line as needed
doctest.testmod
print(need_to_buy_ticket(2,100))