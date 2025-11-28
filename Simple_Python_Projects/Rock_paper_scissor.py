rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
ans = "y"
while ans.lower() == "y":
    option = [rock, paper, scissors]
    try:
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
        if choice < 0 or choice > 2:
            print("You chose an invalid number. You lose!")
        else:
            print(option[choice])
            print("Computer chose...")
            import random
            computer_choice = random.randint(0, 2)
            print(option[computer_choice])

            if choice == computer_choice:
                print("It's a draw")
            elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
                print("You win")
            else:
                print("You lose")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 2.")

    ans = input("Do you want to continue? (y/n): ")
    if ans =="n" :
        print("Thanks for playing! 😎💕")

