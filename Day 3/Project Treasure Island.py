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



print ("Welcome to Treasure Island. \nYour mission is to find the Treasure." )
user = input("You're at a cross road. Where do you want to go? Type" '"left"' " or " '"right"'"\n")

if user != "left":
    print("You fall into a hole. Game Over.")
else:
    user = input("You come to a lake. There is an island in the middle of the lake. Type" '" wait"' "to wait for a boat. Type" '" swim"' "to swim across.""\n")
    if user != "wait":
        print("You got attacked by trout. Game Over.")
    else:
        user = input("You arrive at the island unharmed. There is a house with 3 doors. O red, one yellow and one blue. Wich color do you choose?""\n")
        if user != "yellow" and user == "blue":
            print ("You enter a room of beats. Game Over.")
        elif user != "yellow" and user == "red":
            print ("You enter a room of fire and got burned. Game Over.")
        elif user != "yellow" and user != "red" and user != "blue":
            print ("Game Over.")
        else:
            print("You Win")
