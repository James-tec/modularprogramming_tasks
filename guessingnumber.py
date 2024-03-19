import random


class NumberGuessingGame:

    def __init__(self):

        self.secret_number = random.randint(1, 10)


    def guess_number(self, user_guess):

        if user_guess == self.secret_number:

            return "Congratulations! You guessed the correct number."

        elif user_guess < self.secret_number:

            return "Too low. Try again."

        else:

            return "Too high. Try again."


# Creating NumberGuessingGame object

game = NumberGuessingGame()


# Asking the user to guess the number

while True:

    guess = int(input("Guess the number between 1 and 10: "))

    result = game.guess_number(guess)

    print(result)

    

    # Checking if the guess is correct

    if "Congratulations" in result:

        break

