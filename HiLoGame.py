#K. Davenport
#FOR COLLEGE
#July 11th, 2020
#Hi-Lo Game: This program is a guessing game that asks the user how big of a range they would like to play in, then plays a guessing game with the user.
#Has some minor intelligence to help the user correct their inputs. Today, I'm using f strings for this program (when needed), as well as while not in.

#Sidenote for programmer: research into... if input.lower().startswith("y") by suggestion of Bee from THM.

#We have to import the random library for random number generation.
import random

#This is the outer loop that restarts the game if the user prompts it to.
playAgain = "Yes"
while playAgain in ["Yes", "yes", "y", "Y"]:
    while True:
        gameRange = input("This is a guessing game. Please select how high of a range you would like to play. ")
        #We use .isdigit to figure out if the number our user input is even a number.
        if gameRange.isdigit():
            break
        else:
            #We use an f string to cleanly output the error for the user.
            print(f"We can't use <{gameRange}> as a range. Try again.")

    #This is how we generate our random number, using the imported random library.
    #We have to convert gameRange to an int for the random number generator to work.
    randomNumber = random.randint(1, int(gameRange))

    #Here's the loop for the actual game.
    while True:
        while True:
            userGuess = input ("What do you think the number I'm thinking of is? ")
            if userGuess.isdigit():
                break
            else: print(f"<{userGuess}> is not a number. Try again.")

        userGuess = int(userGuess)
        if userGuess < randomNumber:
            print(f"Your guess of <{userGuess}> is too low. Try again.")
        elif userGuess > randomNumber:
             print(f"Your guess of <{userGuess}> is too high. Try again.")
        else:
            print("You have guessed correctly!")
            break

    #We ask the user if they would like to play again.
    playAgain = input("Would you like to play again?: ")
    #If user does not input a form of yes or no, we tell the user to try again.
    while not playAgain in ["Yes", "No", "yes", "no", "y", "n", "Y", "N"]:
        playAgain = input("Please input a variant of yes or no. ")

    #in []: is awesome for checking user inputs.
    if playAgain in ["No", "no", "n", "N"]:
        print("Thanks for playing with me. I hope to see you again soon!")
    else:
        print("Okay. Let's play again!")
