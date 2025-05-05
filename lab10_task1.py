import doctest

def is_odd(num: int)-> bool:
    """
    Check if a number is odd
    """
    return num % 2 != 0

def separate_numbers(nested_list: list[list[int]]) -> dict[str, dict[str,list[int]]]:
    """
    takes a nested list, separates odd and even numbers within each inner list, and organizes the results in a divctionary_style format.

    >>> separate_numbers([[1, 2, 3, 4, 5], [1, 2, 34, 5]])
    {'list_number_1': {'list': [1, 2, 3, 4, 5], 'odd_numbers': [1, 3, 5], 'even_numbers': [2, 4]}, 'list_number_2': {'list': [1, 2, 34, 5], 'odd_numbers': [1, 5], 'even_numbers': [2, 34]}}
    """
    for inner_list in nested_list:
        for num in inner_list:
            assert isinstance(num, int) and num >= 0, "All elements must be non_negative intergers."

    result_dict = {}

    for i in range(len(nested_list)):
        inner_list = nested_list[i]

        odd_list = []
        even_list = []
        
        for num in inner_list:
            if is_odd(num):
                odd_list.append(num)

            else:
                even_list.append(num)

        list_dict = {
            "list": inner_list, 
            "odd_numbers":  odd_list,
            "even_numbers": even_list
            }
        
        result_dict[f"list_number_{i + 1}"] = list_dict

    return result_dict

doctest.testmod()





