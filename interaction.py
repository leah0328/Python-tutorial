name=input("What is your name? ")


if name=="Tim":
    print("Greetings, Tim the Enchanter")
elif name=="Brian":
    print("Bad luck, Brian")
else:
    print("Hello "+name+".")

def discuss(topic):
    like=input("Do you like "+topic+"?")
    response=input("Why do you think that?")
    return response
            
discuss("university")
print("That's very intersting.")

while True:
    topic =input("What do you want to talk about?")
    if topic =="nothing":
        break
    response=discuss(topic)
    print("I also think that", response)
   
print("Okay. Goodbye,"+name+"!")


