# While Loop - secret word

secret_word = "cat"
guess = " " # need to create a variable to store user input
guess_count= 0
guess_limit= 3
out_of_guess = False

print("Hind: a kind of pet, 3 words.")

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit :
        guess = input("Enter your guess: ")
        guess_count += 1 
    else: 
        out_of_guess= True
        
if out_of_guess:
    print("Out of guesses! You LOSE!") 

else:      
    print("You WIN!")




 

