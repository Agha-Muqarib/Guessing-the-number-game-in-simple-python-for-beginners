
import random

def guess_it():

    print("\n", "Welcome to Guessing game. You will be asked for the number I will be having in mind. Let's start \n")
    actual_number = random.randint(0, 10)
    tries = 3

    while True:
        if tries == 0:
            print("You lose, the actual number was ", actual_number, "!")
            print("Game Over")
            break

        else:
            guessed_number = int(input("Guess your number:  "))
            if guessed_number < 0 or guessed_number > 10:
                raise Exception("Value Error: Enter number between 0-10 !")

            else:
                
                if guessed_number < actual_number:
                    print("The guessed number is less than actual number")
                    tries -= 1
                    print("You've {} tries left".format(tries), "\n")

                elif guessed_number > actual_number:
                    print("The guessed number is greater than actual number")
                    tries = tries-1
                    print("You've {} tries left".format(tries), "\n")

                elif guessed_number == actual_number:
                    print("Congratulations, You guessed the right number!", "\n")
                    break
            
# Driver Code

guess_it()