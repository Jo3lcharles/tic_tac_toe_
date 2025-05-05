#1. Take the input in the the format of "x # y"
user_input = input("Please provide an expression in the format of x #y: ")

#2. Do some calculation with the input 
#2.1 Find x and y in "x # y"
#2.1.1 Find where '#' is 
pound_index = user_input.find('#')

#2.1.2 Find what the numbr is before '#' and let it be x
x = int(user_input[:pound_index])

#2.1.3 Find what the numbr is after '#' and let it be x
y =  int(user_input[pound_index + 1:])

#2.2 Calculate the result base on the definition of '#'
#x #y  = x2- y2
result = x ** 2 - y ** 2

#show the result 
print(result)

