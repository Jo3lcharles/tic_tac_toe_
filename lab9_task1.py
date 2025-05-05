import doctest

def merge_lists(list_1:list[int], list_2:list[int])-> list[int]:
    """
    Merge 2 sorted lists into 1

    >>> merge_lists([0,1,2,3], [6,7,8])
    [0, 1, 2, 3, 6, 7, 8]
    >>> merge_lists([0,1,3,5], [0,1,2,4,6])
    [0, 0, 1, 1, 2, 3, 4, 5, 6]
    >>> merge_lists([], [1,5,10])
    [1, 5, 10]

    """
    assert is_sorted(list_1), "list_1 unsorted"
    assert is_sorted(list_2), "list_2 unsorted"

    i = 0
    j = 0

    merged_list = []
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            merged_list.append(list_1[i])
            i+=1
        else:
            merged_list.append(list_2[j])
            j += 1

    if i >= len(list_1):
        merged_list.extend(list_2[j:])
    else:
        merged_list.extend(list_1[1:])


    return merged_list

def is_sorted(nums: list[int])-> bool:
    """
    determine if a list is sorted

    >>> is_sorted([1, 2, 2, 3, 4])
    True
    >>> is_sorted([9,5,10])
    False
    >>> is_sorted([6])
    True
    """
    assert type(nums) == list, "the input must be a list"

    i = 1

    while i < len(nums):
        if nums[i] < nums[i - 1]:
            return False
        i += 1
    return True

doctest.testmod()
