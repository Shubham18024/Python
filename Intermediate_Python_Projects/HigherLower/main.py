#Importing necessary module and art
from game_data import data
from art import *
from random import randint
from os import system,name


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def get_data(first_account):
    """returns unique second_account"""
    second_account = data[randint(0, len(data) - 1)]
    while first_account == second_account:
        second_account = data[randint(0, len(data) - 1)]
    return second_account


def is_correct_guess(user_choice, account_a_followers, account_b_followers):
    """evaluate user's choice and it responds accordingly"""
    if user_choice == 'A' and account_a_followers > account_b_followers :
        return True
    elif user_choice == 'B' and account_a_followers < account_b_followers:
        return True
    else :
        return False


def clear_screen() -> None:
    """clears terminal screen"""
    try:
        system('cls' if name == 'nt' else 'clear')
    except OSError:
        pass


def main() -> None:
    """Handles main game play"""
    keep_playing = True
    current_score = 0
    account_a = data[randint(0, len(data) - 1)]
    while keep_playing:
        clear_screen()
        print(logo)
        if current_score > 0:
            print(f"You're right!🥳 Current Score: {current_score}")
        account_b = get_data(account_a)
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        user_input = input("Who has more followers? Type 'A' or 'B': \t").upper()
        is_correct = is_correct_guess(user_input, account_a['follower_count'], account_b['follower_count'])
        if is_correct:
            current_score += 1
            account_a = account_b
        else :
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
            keep_playing = False


if __name__ == "__main__":
    while True:
        main()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye. 👋")
            break