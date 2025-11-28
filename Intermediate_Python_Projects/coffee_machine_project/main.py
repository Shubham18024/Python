from data import MENU, resources


def check_ingredients(ingredients_list):
    for ingredient in ingredients_list:
        if ingredients_list[ingredient] <= resources[ingredient]:
            continue
        else:
            return ingredient
    return True


def validate_coins(number_of_coins, original_amount, coin_value):
    amount = 0
    for quantity, value in zip(number_of_coins.values(), coin_value.values()):
        amount += quantity * value
    if amount < original_amount:
        return False
    else:
        return round(amount - original_amount, 2)


def update_resources(ingredients_list,original_amount):
    for ingredient in ingredients_list:
        resources[ingredient] -= ingredients_list[ingredient]
    resources["Money"] += original_amount


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['Money']}")
    elif user_input == "off":
        exit()
    else:
        lst_of_ingredients = MENU[user_input]["ingredients"]
        coffee_amount = MENU[user_input]["cost"]
        output = check_ingredients(lst_of_ingredients)
        if output is not True:
            print(f"Sorry there is not enough {output}.")
        else:
            print(f"Please insert coins")
            coins = {}
            value_of_coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
            for coin in ["quarters", "dimes", "nickles", "pennies"]:
                coins[coin] = int(input(f"how many {coin} do you have? "))
            return_amount = validate_coins(coins, coffee_amount, value_of_coins)

            if return_amount:
                update_resources(lst_of_ingredients, coffee_amount)
                print(f"here is ${return_amount} in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")