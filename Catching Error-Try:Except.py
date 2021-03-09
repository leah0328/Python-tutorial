# Try / Except block : for times when something goes wrong
# eg. user insert an indesired input

try:
    answer=10/0
    number=int(input("Enter a number: "))
    print(number)

except ZeroDivisionError:
    print("Invalid Input")
except ValueError:
    print("Value Input")

#we can also store the ErrorType as a variable, see ##
try:
    number=int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err: ## 
    print("err") # in this way, it will print out what went wrong,
                 # instead of the error type
except ValueError:
    print("Value Input")
    
# Best practice is to specify the return value according to the Error type
# otherwise it is too broad(people wouldnt know what went wrong)