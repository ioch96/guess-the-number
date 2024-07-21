# Import the random module to generate random numbers
import random

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
        elif guess < random_number:
			# Inform the user if the guess is too low
            print("Too low")
        else:
			# Inform the user if the guess is too high
            print("Too high")

    except ValueError:
        # Handle the case where the user input is not a valid integer
        print("Invalid input. Please enter an integer.")

# Print a congratulatory message including the number of attempts taken
print(f"Good job! You guessed the number {random_number} in {attempts} attempts")
