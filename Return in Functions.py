# Return in Functions

def cube(num):
    num*num*num

cube(3)
# in this case python will return 'none', so we have to

def cube_1(num):
    return num*num*num
 
result=cube_1(3)
print(result)

