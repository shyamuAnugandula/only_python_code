# Question
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place,
# they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
# tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
# Say the number generated by the computer is 1038. An example interaction could look like this:
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.


#_______________________________________________ With String __________________________________________________

import random

cows = 0   # initial setting as 0 cows
bulls = 0   # initial setting as 0 cows
generated_guess_number = str(random.randint(1000,9999))  # generating 4 digit number and then into string
#print(generated_guess_number)  # printing the randomly generated number
user_entered = str(input("Guess 4 digit number correctly")) # Asking user to input to guess number
trails = 1  # no of guesses
while(True):
    if(generated_guess_number == user_entered):  # if true will get executed
        print(f"Game Over !!!  ***Awesome*** You have guessed this in {trails} trials")
        break
    else:  # If incorrect guess
        for i in range(len(user_entered)):
            if generated_guess_number[i] == user_entered[i]: # if both alphabet match
                # print(f"{k[i]} and {j[i]}") #To know which element is correct
                cows += 1  # increment cow count
            else:  # if both alphabet do not match
                bulls +=1  # increment bull count
        print(f"You have {cows} cows & {bulls} bulls !!! Try again until you get all cows")   # For each trail print for user to understand
        user_entered = str(input("Enter 4 digit number"))
        if (generated_guess_number == user_entered): # if true will get executed
            print(f"Game Over !!! You have guessed this in {trails} trials")
            break # break the loop if condition is true
        cows = 0  # count making 0 to run loop for second trail with start
        bulls = 0  # count making 0 to run loop for second trail with start
        trails += 1  # increasing trail for each itteration



#___________________________________________________ With Str to List ____________________________________________



import random

cows = 0   # initial setting as 0 cows
bulls = 0   # initial setting as 0 cows
generated_guess_number = random.randint(1000,9999)  # generating 4 digit number
string = str(generated_guess_number) # converting generated number to string
generated_guess_number1 = string.split(' ') # converting string into list
print(generated_guess_number1)  # printing the randomly generated number
user_entered = str(input("Guess 4 digit number correctly")) # Asking user to input to guess number
user_entered = user_entered.split(' ')
trails = 1  # no of guesses
while(True):
    if(generated_guess_number1 == user_entered):  # if true will get executed
        print(f"Game Over !!!  ***Awesome*** You have guessed this in {trails} trials")
        break
    else:  # If incorrect guess
        for j in generated_guess_number1: # first element from the random generated list
            for k in user_entered:  # first element from the user input list
                for i in range(0,4):  # no of itteration to check value at position
                    if k[i] == j[i]: # if both alphabet match
                        # print(f"{k[i]} and {j[i]}")
                        cows += 1  # increment cow count
                    else:  # if both alphabet do not match
                        bulls +=1  # increment bull count
        print(f"You have {cows} cows & {bulls} bulls !!! Try again until you get all cows")   # For each trail print for user to understand
        user_entered = str(input("Enter 4 digit number"))
        user_entered = user_entered.split(' ')
        if (generated_guess_number1 == user_entered): # if true will get executed
            print(f"Game Over !!! You have guessed this in {trails} trials")
            break # break the loop if condition is true
        cows = 0  # count making 0 to run loop for second trail with start
        bulls = 0  # count making 0 to run loop for second trail with start
        trails += 1  # increasing trail for each itteration
