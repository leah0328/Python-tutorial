# Writing to Files

# before we do anything, make sure the file is readable with:
employee_file=open("abc.txt","r")
print(employee_file.readable())
employee_file.close()

#______________________________#

employee_file=open("abc.txt","a")
print(employee_file.write("Toby-Human Resources"))
employee_file.close()

# and the line will be appended to the txt on a new line_________
# but if you run it a again another line will be added to the same line

# so we could do this instead:
employee_file=open("abc.txt","a")
print(employee_file.write("\nToby - Human Resources"))
employee_file.close()
#______________________________#


# Using 'w', will override the ecxisting data, and overwrite the file
employee_file=open("abc.txt","w")
print(employee_file.write("\nKelly - Customer service"))
employee_file.close()
#______________________________#

# if we change the name of the txt, it will automatically create a new file
employee_file=open("abc123.txt","w")
print(employee_file.write("\nnew flie 1st line"))
employee_file.close()
#______________________________#

# we could also create a webpage with this function
employee_file=open("index.html","w")
print(employee_file.write("<p>This is HTML</p>"))
employee_file.close()
