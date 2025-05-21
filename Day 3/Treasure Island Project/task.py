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
name = input("What is your adventurer name?")
decision_1 = input("Hello," + name + "you are at a crossroad. Where do you want to go? left or right?")
if decision_1 == "right":
    print("You fell into a hole and DIED. Game Over!")
elif decision_1 == "left":
    decision_2 = input("You've come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across.")
    if decision_2 == "swim":
        print("Attacked by killer trout. Game Over!")
    elif decision_2 == "wait":
        decision_3 = input("You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if decision_3 == "red":
            print("It's a room full of fire. Game Over")
        elif decision_3 == "yellow":
            print("You found the treasure. You Win!")
        elif decision_3 == "blue":
            print("You enter a room of beasts. Game Over.")
else:
    print("You chose poorly, game over!")