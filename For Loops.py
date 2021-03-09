# For Loop 

# Example 1
rainbow = ["red", "yellow" ,"green", "blue"]
for colour in rainbow:
    print(colour)

# Example 2
for letter in "ありがとうございます":
    print(letter)

# Example 3
for index in range(8):
    print(index)

# Example 4
for index in range(3,8,2): 
    #will print out numbers starting from 3 to 8 but not including 8
    print(index)

# Example 5
for index in range(3,8,2): 
    #will print out every 2nd numbers starting from 3 to 8 but not including 8
    
# Example 6 **
friends = ["Rachel", "Ross", "Monica"] 
for index in range(len(friends)):
    print(friends[index])
 
#Example 7 **
friends = ["Rachel", "Ross", "Monica"] 
for index in range(5):
    if index == 0:
        print ("First iteration")
    else:
        print ("Not first")
