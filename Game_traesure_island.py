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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to treasure island.")
print("Your mission is to find the treasure.")
choice1 = input("You are at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()
if choice1 == "left":
    choice2 = input("You have come to lake. There is an island in the middle lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if choice2 == "wait":
        choice3 = input("You have arrived at island unharmed. There are house with 3 doors. one red, one yellow and one blue. which colour do you choose?\n").lower()
        if choice3 == "red":
            print("You Burned by fire, Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure, You win.")
        elif choice3 == "blue":
            print("You get eaten by the beasts, Game Over.")
        else:
            print("You choose the the door that doesn't exist.")
    else:
        print("You attacked by trout, Game over.")
else:
    print("You fell into hole, Game Over.")