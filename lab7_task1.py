import doctest

ALLOWED_NUMBER = 5

def calculate_average(numbers_str : str)-> float:
    """
    Returns average of numbers

    >>> calculate_average("1|2|3|4|5")
    3.0
    >>> calculate_average("2 |  10|  5|7|11")
    7.0
    """

    assert type(numbers_str) == str, "The input must  be string"

    numbers = numbers_str.split('|')

    assert len(numbers) == ALLOWED_NUMBER, "Input string contain exactly 5 numbers."

    total = 0
    total = total + int(numbers[0].strip())
    total = total + int(numbers[1].strip())
    total = total + int(numbers[2].strip())
    total = total + int(numbers[3].strip())
    total = total + int(numbers[4].strip())

    average = total / ALLOWED_NUMBER

    return average

doctest.testmod()
