import random

random_number = random.randint(0, 100)
attempts = 0

while True:
    attempts += 1
    guess = int(input('Enter your guess:\t'))
    if guess == random_number:
        break
    elif guess < random_number:
        print('Too low')
    else:
        print('Too high')

print(f'Good job! You guessed the number in {attempts} attempts')
