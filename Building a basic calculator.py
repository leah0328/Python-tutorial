# Building a basic calculator

print("Example 1")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)

# The result was not the '+' function that we expected.
# Because python think of the user input as a [string], 
# where a number should be an [integer: whole number , no decimal point/fraction]
# so to achieve the result we wanted, convert the [str] to [int]

print("Example 2")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)

print(result)

# Error will occur if a number with decimal in inserted
# as [int] is only for whole number
# so far number with decimal, use [float: decimal number] instead 

print("Example 3")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)
