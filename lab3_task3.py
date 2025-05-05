# get input
age = int(input("What is the child's age? "))
height = int(input("What is the child's height? "))

# you can add any line of code between this line and the line with return
x = age > 6
y = height > 120

result = ((x or y) and y) or x
# show result
print(result) # You should modify this line as needed
