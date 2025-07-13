from random import choice
import art
import os


def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except OSError:
        pass


def choice_of_cards(number_of_cards: int):
    for _ in range(number_of_cards):
        yield choice(cards)


def is_blackjack(player_cards, dealer_cards):
    player_blackjack = sum(player_cards) == 21 and len(player_cards) == 2
    dealer_blackjack = sum(dealer_cards) == 21 and len(dealer_cards) == 2
    if player_blackjack and not dealer_blackjack:
        print("🥳 BLACKJACK, Congratulations you win!")
        return None
    elif dealer_blackjack and not player_blackjack:
        print("😔 Oops, you lost!")
        return None
    elif player_blackjack and dealer_blackjack:
        print("🥱 PUSH, Match gets Draw")
        return None
    else:
        return False


def adjust_ace(cards_list):
    """Adjusts Ace (11 → 1) if total goes above 21. Keeps adjusting if needed."""
    while 11 in cards_list and sum(cards_list) > 21:
        index = cards_list.index(11)
        cards_list[index] = 1


def print_final_hands(player_cards, dealer_cards):
    print(f'   Your final hand: {player_cards}, final score : {sum(player_cards)}')
    print(f'   Computer\'s final hand: {dealer_cards}, final score : {sum(dealer_cards)}')


# 🔁 Game replay loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower() == 'y':
    clear_screen()
    print(art.logo)
    keep_playing = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_cards_player = list(choice_of_cards(2))
    drawn_cards_dealer = list(choice_of_cards(2))

    while keep_playing:
        adjust_ace(drawn_cards_player)  # ✅ Make sure to adjust before checking score
        sum_player_cards = sum(drawn_cards_player)
        print(f'    Your drawn cards are: {drawn_cards_player}, current score : {sum_player_cards}')
        print(f'    Computer\'s first card: {drawn_cards_dealer[0]}')

        blackjack_result = is_blackjack(drawn_cards_player, drawn_cards_dealer)
        if blackjack_result is False:
            if sum_player_cards > 21:
                print_final_hands(drawn_cards_player, drawn_cards_dealer)
                print("😔 You went over. Oops, you lost!")
                keep_playing = False
                break

            player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_choice == 'y':
                drawn_cards_player.append(next(choice_of_cards(1)))
            else:
                # Dealer's turn
                adjust_ace(drawn_cards_dealer)
                while sum(drawn_cards_dealer) < 17:
                    drawn_cards_dealer.append(next(choice_of_cards(1)))
                    adjust_ace(drawn_cards_dealer)

                print_final_hands(drawn_cards_player, drawn_cards_dealer)

                if sum(drawn_cards_dealer) > 21:
                    print(f"🥳 Dealer went over\nCongratulations you win!")
                elif sum(drawn_cards_dealer) > sum_player_cards:
                    print("😔 Oops, you lost!")
                elif sum(drawn_cards_dealer) == sum_player_cards:
                    print("🥱 PUSH, Match gets Draw")
                else:
                    print("🥳 Congratulations you win!")
                keep_playing = False
                break
        else:
            keep_playing = False
