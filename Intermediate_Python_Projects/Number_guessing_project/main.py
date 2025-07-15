from random import randint
from art import logo

def checker(number_of_attempts, number):
    """Track Number of attempts, check answer against guess and print the result accordingly."""
    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        try :
            guess = int(input("Make a guess:    "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess == number :
            print(f"You got it! The answer was {number}")
            break
        else :
            number_of_attempts -= 1
            if number_of_attempts == 0:
                print(f"You've run out of guesses. Try again!\nThe correct answer was {number}")
                break
            if guess > number:
                print("Your guess is too high.\nGuess again.")
            elif guess < number:
                print("Your guess is too low.\nGuess again.")


def main():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard':    ")
    number = randint(1, 100)
    match user_choice:
        case "hard":
            hard_level_turns = 5
            checker(hard_level_turns, number)
        case "easy":
            easy_level_turns = 10
            checker(easy_level_turns, number)
        case _:
            print("Sorry, you didn't choose a valid type.")


if __name__ == "__main__":
    while True:
        main()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye. 👋")
            break