# If statement - comaprison

def max_num (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1

    elif n2 > n3 and n2 > n1:
        return n2

    elif n3 > n1 and n3 > n2:
        return n3
       

print(max_num (96,2,16))
# dont forget [print]!
# a more simplified code would be to replace line 10 to -> else:

def max_num (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1

    elif n2 > n3 and n2 > n1:
        return n2

    else:
        return n3

# comparison operator: (str can be compare as well)
    > greater than
    < less than
    >= greater then or equal to
    <= less than or equal to
    == equals (to compare values)
    != not equal