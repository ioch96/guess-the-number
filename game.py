import random

# Generate a random number between 0 and 100 (inclusive)
random_number = random.randint(0, 100)

# Initialize attempts counter
attempts = 0

# Start an infinite loop to allow multiple guesses until the correct number is guessed
while True:
    # Increment the attempts counter
    attempts += 1
    
    # Prompt the user to enter their guess and convert it to an integer
    guess = int(input('Enter your guess:\t'))
    
    # Check if the guess matches the randomly generated number
    if guess == random_number:
        # If the guess is correct, break out of the loop
        break
    elif guess < random_number:
        # If the guess is lower than the random number, inform the user
        print('Too low')
    else:
        # If the guess is higher than the random number, inform the user
        print('Too high')

# Print a congratulatory message along with the number of attempts taken
print(f'Good job! You guessed the number {random_number} in {attempts} attempts')
