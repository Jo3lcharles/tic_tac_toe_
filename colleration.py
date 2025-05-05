def separate_numbers(nested_list:list[list[int]]) -> dict[str,dict[str, list[int]]]:
    #make sure the input is a list
    assert isinstance(nested_list,list), "invalid argument"
    #ensure it has an inner loop and the inner loop contains intergers
    for list_ in nested_list:
        if not isinstance(list_, list):
            raise AssertionError("invalid argument")
        for element in list_:
            if not isinstance(element, int):
                raise AssertionError("invalid argument")
            
    outer_dict = {}   
    for i , inner_list in enumerate(nested_list):
        odd_list = [x for x in inner_list if x%2 != 0]
        even_list = [x for x in inner_list if x%2 == 0]
        inner_dict = {"list" : inner_list , "odd" : odd_list, "even" : even_list}
        outer_dict[f"list_number_{i}"] = inner_dict

    return outer_dict



from statistics import mean

def co_efficient(list_1: list[int], list_2:list[int]):
    avg_ref = mean(list_1)
    avg_list = mean(list_2)
    numerator = 0
    denominator1 = 0
    denominator2 = 0

    for a,b in zip(list_1 , list_2):
        difference1 = a - avg_ref
        difference2 = b - avg_list
        numerator+=(difference1 * difference2)
        denominator1 +=difference1**2
        denominator2 += difference2**2

    denominator = (denominator1 * denominator2)** 0.5

    if denominator == 0:
        raise AssertionError("denominator cant be 0")
    else:
        co_efficient = numerator/ denominator

    return co_efficient


def highest_col(ref:list[int], nested_list: list[list[int]]):
    compare = []
    for list_ in nested_list:
        if len(list_) != len(ref):
            raise AssertionError(" inner list must be of the same length as the reference list")
    for sublist in nested_list:
        co_efficient_ = co_efficient(ref, sublist)

        compare.append(co_efficient_)
    return (nested_list[compare.index(max(compare))] , round(max(compare), 4))