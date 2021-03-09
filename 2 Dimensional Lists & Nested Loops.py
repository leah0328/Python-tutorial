# 2 Dimensional Lists & Nested Loops

number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]
# so inside the 'number_grid'list, 
# the elements are also a list (4 elelment which are all list )

# it is actually a grid
# there is 4 rows & 3 columns
# or in python there (0,1,2,3)rows & (0,1,2)columns

# To access individual element in the big list,
# insert the index of the element you wanted to access
print(number_grid[3][0])
 #so if it's row[2], column[1], which will be '8'
 # or if its [0][0], it would be '1' 

# Nested For Loops = a for loops inside of a for loops
for row in number_grid:
    print(row)

for row in number_grid:
     for col in row:
         print (col)
