
name=input("What is your name?")
if name=="Tim":
    print("Greetings, Tim the Enchanter")
elif name=="Brian":
    print("Bad luck, Brian")
else:
    print("Hello"+name+".")

like=input("Do you like university?")
response=input("Why do you think that?")
print("That's very intersting.")

while True:
    topic =input("What do you want to talk about?")
    if topic =="nothing":
        break
    like=input("Do you like"+topic+"?")
    response=input("Why do you think that?")
    print("I also think that", response)
   
print("Okay. Goodbye,"+name+"!")


