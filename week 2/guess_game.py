import random

print("--- Guess the Number Game ---")

# 1. Computer picks a number
secret_number = random.randint(1, 20)
guess = 0 # Initialize with a number that cannot be the answer
attempts = 0

# 2. Loop until the user gets it right
while guess != secret_number:
    # Get input
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1
    
    # Check logic
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")