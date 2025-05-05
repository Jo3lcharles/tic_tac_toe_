import doctest

APPLE = "apple"
BANANA = "banana"
GRAPE = "grape"
ORANGE = "orange"
shit = [APPLE,BANANA,GRAPE,ORANGE]

def list_to_dict(input_list: list[int]) -> dict[str, int]:
    """
    Converts a list into a dictionary 
    where the keys are the indices of the elements in the list.
    
    Parameters:
        input_list (list): The input list to be converted.
        
    Returns:
        dict: A dictionary where keys are strs 
        and values are elements from the list.
    
    >>> list_to_dict([10, 15, 20, 25])
    {'apple': 10, 'banana': 15, 'grape': 20, 'orange': 25}
    >>> list_to_dict([1, 5, 20, 25])
    {'apple': 1, 'banana': 5, 'grape': 20, 'orange': 25}
    >>> list_to_dict([10, 10, 10, 10])
    {'apple': 10, 'banana': 10, 'grape': 10, 'orange': 10}
    >>> list_to_dict([])
    Traceback (most recent call last):
    ...
    AssertionError: there must be 4 elements in the list
    >>> list_to_dict([30, 10, 4])
    Traceback (most recent call last):
    ...
    AssertionError: there must be 4 elements in the list
    >>> list_to_dict([0.3, 10, 4, 6])
    Traceback (most recent call last):
    ...
    AssertionError: the element must be a non-negative int
    >>> list_to_dict([-3, 10, 4, 6])
    Traceback (most recent call last):
    ...
    AssertionError: the element must be a non-negative int
    >>> list_to_dict([0.9, 10, 4, 6])
    Traceback (most recent call last):
    ...
    AssertionError: the element must be a non-negative int
    >>> list_to_dict([5, 10, 15])
    Traceback (most recent call last):
    ...
    AssertionError: there must be 4 elements in the list
    >>> list_to_dict([0.5, 5, 10, 15])
    Traceback (most recent call last):
    ...
    AssertionError: the element must be a non-negative int
    """
    
    assert type(input_list) == list, "the input must be a list"

    assert len(input_list) == 4, "there must be 4 elements in the list"
    
    assert type(input_list[0]) == int and input_list[0] >= 0, "the element must be a non-negative int"
    assert type(input_list[1]) == int and input_list[1] >= 0, "the element must be a non-negative int"
    assert type(input_list[2]) == int and input_list[2] >= 0, "the element must be a non-negative int"
    assert type(input_list[3]) == int and input_list[3] >= 0, "the element must be a non-negative int"

    result = {}
    for item, quantity in zip(shit,input_list):
        result[item] = quantity

    return result

doctest.testmod()


print(list_to_dict([10, 15, 20, 25]))

