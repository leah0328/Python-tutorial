#Using Funnction with List

numbers=[2,4,6,8,10,12]
friends= ["Robin", "Barney", "Marshal", "Lily", "Ted", "Victoria"]

# To combine one list to another, use [extend]

friends.extend(numbers)
print(friends)

# To add more values to a list, use [append]
# the value will be added onto the END of the list

numbers.append(14)
print(numbers)

# To add the values in a certain place, 
# use [insert], with (index[place you wanted the value to be], "the value you wanted to add") 

countries= ["Malaysia", "USA", "Britain", "Japan", "Australia", "Korea"]

countries.insert(3, "Thailand")
print(countries)

# To remove a certain value, use [remove]

colour= ["Red", "White", "Yellow"]
colour.remove("White")
print(colour)