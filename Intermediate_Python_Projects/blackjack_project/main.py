from game_data import data
from art import *
from random import randint


def get_data() -> dict:
    """returns random data from the game_data"""
    return data[randint(0, len(data) - 1)]


def main() -> None:
    print(logo)
    current_score = 0
    x = get_data()
    y = get_data()
    print(f"Compare A: {x['name']}, a {x['description']}, from {x['country']}.")
    print(vs)
    print(f"Against B: {y['name']}, a {y['description']}, from {y['country']}.")


if __name__ == "__main__":
    main()
