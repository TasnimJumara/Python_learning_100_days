print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

print("You are at a cross road. Where do you want to go?")
choice_1 = input("Type 'left' or 'right'\n").lower()

if choice_1 == "left":
    print("You have come to a lake. There is an island in the middle of the lake.")
    choice_2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    if choice_2 == "wait":
        print('You arrive at the island unharmed. There\'s a house with 3 doors. '
              'Which door do you want to choose?')
        choice_3 = input("Type Red, Blue or Yellow.\n").lower()

        if choice_3 == "red":
            print("You are burned by a fire. Game Over!")
        elif choice_3 == "blue":
            print("You are eaten by beasts. Game Over!")
        elif choice_3 == "yellow":
            print("Hurrah! You find the treasure. You win.")
        else:
            print('You chose a wrong door that doesn\'t exist. Game Over!')
    else:
        print("You are attacked by a trout. Game over!")
else:
    print("You fall into a hole. Game Over!")
