import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    # Check if the input is a valid number
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        # Check if the guess is within the valid range
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        # Check if the guess is too low or too high
        elif guess < answer:
            print("Too low! Try again!")

        elif guess > answer:
            print("Too high! Try again!")

        # Correct guess
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False  # Stop the game

    else:
        # Invalid guess (non-numeric input)
        print("Invalid guess. Please enter a number.")
        print(f"Please select a number between {lowest_num} and {highest_num}")
