print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction = input("You're at a crossroad, which direction should we go, left or right?\n").lower()
if direction == "left":
    print(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    swim_or_wait = input("Which one will you choose, swim or wait?\n")
    if swim_or_wait == "wait":
        print("You waited for a boat and safely crossed the lake. You proceed to the next part of your adventure.")
    elif swim_or_wait == "swim":
        print("Attacked by trout. Game Over.")
    else:
        print(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        door_color = input("Red, Yellow or Blue?\n").lower()
    if door_color == "red":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
    door_color = input("Red, Yellow or Blue?\n").lower()
    if door_color == "red":
        print("It's a room full of fire. Game Over.")
    elif door_color == "yellow":
        print("You found the treasure. You Win!")
    elif door_color == "blue":
        print("You enter a room of beasts. Game Over.")
    else:
        print("You chose a door that doesn't exist. Game Over.")
elif direction == "right":
    print("Fall into a hole. Game Over.")
