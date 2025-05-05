import doctest

def absolute_value(number: str)-> float:
    """
    Return the absolute value of a floating number

    >>> absolute_value("|2.3|")
    2.3
    >>> absolute_value("|-3|")
    3.0
    >>> absolute_value("|0|")
    0.0
    >>> absolute_value("  |-3|  ")
    3.0
    >>> absolute_value(32)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument
    >>> absolute_value("|a|")
    Traceback (most recent call last):
    ...
    AssertionError: input should be a real number

    >>> absolute_value("|2||")
    Traceback (most recent call last):
    ...
    AssertionError: not the number of strips needed

    >>> absolute_value("|3")
    Traceback (most recent call last):
    ...
    AssertionError: not the number of strips needed

    >>> absolute_value("||2")
    Traceback (most recent call last):
    ...
    AssertionError: strips should be at the beginning and at the end

    >>> absolute_value("|2.9.9|")
    Traceback (most recent call last):
    ...
    AssertionError: one decimal point should be used

    >>> absolute_value("|.9|")
    Traceback (most recent call last):
    ...
    AssertionError: decimal point should be in between the numbers

    >>> absolute_value("|9.|")
    Traceback (most recent call last):
    ...
    AssertionError: decimal point should be in between the numbers

    >>> absolute_value("|sd3|")
    Traceback (most recent call last):
    ...
    AssertionError: input should be a real number

    >>> absolute_value("|6-|")
    Traceback (most recent call last):
    ...
    AssertionError: negative sign should be before the number

    >>> absolute_value("|--6|")
    Traceback (most recent call last):
    ...
    AssertionError: only one negative sign should be used

    >>> absolute_value("||")
    Traceback (most recent call last):
    ...
    AssertionError: no number found


    """

    assert type(number) == str, "invalid argument"

    #remove all white space
    number = number.strip()

    #check for strip location and number
    check1 = number.count("|")
    assert check1 == 2 , "not the number of strips needed"

    check2 = number[0]
    assert check2 == "|", "strips should be at the beginning and at the end"

    check3 = number[-1]
    assert check3 == "|", "strips should be at the beginning and at the end"

    #check for decimal points
    check4 = number.count(".")
    assert check4 <= 1, "one decimal point should be used"

    #check for negative sign
    check5 = number.count("-")
    assert check5 <= 1, "only one negative sign should be used"


    #remove strips
    rm_strips = number.replace("|", "").strip()

    assert rm_strips != "", "no number found" #ensure not an empty string

    assert rm_strips[0] != ".", "decimal point should be in between the numbers" #ensure no decimal at the beginning
    assert rm_strips[-1] != ".", "decimal point should be in between the numbers" #ensure no decimal at the beginning

    check6 = "-" in rm_strips[1:]
    assert check6 == False, "negative sign should be before the number" #ensure negative sign is at the beginning

    assert (rm_strips.replace("-", "").replace(".", "")).isnumeric() == True, "input should be a real number" #ensure only numbers are used


    final = abs(float(rm_strips))

    return final


doctest.testmod()



    