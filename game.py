"""
Number Guessing Game

This module allows the user to guess a randomly generated number between 0 and 100.
The user receives feedback on whether their guess is too low or too high, and the
number of attempts taken to guess the correct number is tracked and displayed.
"""

import random

def main():
    """
    Main function to run the number guessing game.

    This function generates a random number between 0 and 100 and prompts the user to
    guess the number. It provides feedback on whether the guess is too low or too high
    and keeps track of the number of attempts the user takes to guess the correct number.
    """
    # Generate a random integer between 0 and 100 (both included)
    random_number = random.randint(0, 100)

    # Initialize a counter to keep track of the number of attempts
    attempts = 0

    # Start an infinite loop to allow continuous guessing until the correct number is guessed
    while True:
        try:
            # Prompt the user to enter a guess and convert the input to an integer
            guess = int(input("Enter your guess (0-100): "))

            # Check if the guess is within the valid range
            if guess < 0 or guess > 100:
                print("Please enter a number between 0 and 100.")
                # If not, prompt the user again without counting this attempt
                continue

            # Increment the attempts counter only for valid inputs
            attempts += 1

            # Check if the guess matches the randomly generated number
            if guess == random_number:
                # If the guess is correct, exit the loop
                break
            if guess < random_number:
                # Inform the user if the guess is too low
                print("Too low")
            else:
                # Inform the user if the guess is too high
                print("Too high")

        except ValueError:
            # Handle the case where the user input is not a valid integer
            print("Invalid input. Please enter an integer.")

    # Print a congratulatory message including the number of attempts taken
    print(f"\nGood job! You guessed the number {random_number} in {attempts} attempts")

if __name__ == "__main__":
    main()
