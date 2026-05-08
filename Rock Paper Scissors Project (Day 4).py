import random

print("Welcome to Rock, Paper and Scissors Game!")

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
---'    ____)____
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

game = [rock, paper, scissors]
game_index = random.randint(0, 2)
computer_choice = game[game_index]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if (user_choice >= 0) and (user_choice <= 2):
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {game[user_choice]}")

    if user_choice == game_index:
        print("Hey, it's a draw.")
    elif (user_choice == 0) and (game_index == 2):
        print("Hurrah! You won.")
    elif (user_choice == 2) and (game_index == 0):
        print("Computer won.")
    elif game_index > user_choice:
        print("Computer won.")
    elif user_choice > game_index:
        print("Hurrah! You won.")

else:
    print("Sorry, you've given a wrong input.")