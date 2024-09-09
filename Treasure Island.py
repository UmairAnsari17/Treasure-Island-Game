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
print("Your mission is to find the treasure.")
chose1 = input('You\'re at a cross road. Where do you want to go?\n Type "left" or "right". \n').lower()
if chose1 == "left":
    chose2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to Wait for boat.Type "swim" to Swim across.\n').lower()
    if chose2 == "wait":
        chose3 = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow, one blue. Which colour do you want to chose?\n").lower()
        if chose3 == "yellow":
            print("You found the treasure! You Win!")
        elif chose3 == "red":
            print("Burned by fire. Game Over.")
        else:
            print("Eaten by beasts. Game Over.")
    else:
        print("you get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

