# get input
# type 1 for True, press enter without input any value is False
a = bool(input("a = "))
b = bool(input("b = "))
    
# do the calculation
# The result is True iff it is not both True and both False
is_both_true = a or b
is_both_false = a and b
    
result = is_both_true and not is_both_false
    
# show the result
print(result)