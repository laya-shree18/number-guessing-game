import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts_allowed = 7

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts_allowed} attempts to guess it.")

    for attempt in range(1, attempts_allowed + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
    else:
        print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")

number_guessing_game()

