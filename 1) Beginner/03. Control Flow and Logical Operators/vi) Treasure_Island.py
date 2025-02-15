"""
  ASCII art -  https://ascii.co.uk/art
  
  Reffer - Treasure_Island_Flowchart.jpg

"""



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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("\nFirst Challenge:-")
left_or_right = input("You're at a cross road. Where do you want to go? Type 'Left' or 'Right'\n")
left_right = left_or_right.lower()

if left_right == 'left' :
  print("\nSecond Challenge:-")
  wait_or_swim = input("You've come to a lake. There is an Island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
  wait_swim = wait_or_swim .lower()  

else :
  print("You fell into a hole. GAME OVER!")
  exit()
  
if wait_swim == 'wait' :
  print("\nFinal Challenge:-")
  colour = input("You arrive at the Island unharmed. There is a house with 3 doors. One Red, one Yellow and one Blue. Which colour do you choose?\n")
  lower_colour = colour.lower()

else :
  print("You get attacked by an angry trout. GAME OVER!")
  exit()

if lower_colour == 'red' :
  print("It's a room full of fire. GAME OVER!")
  
elif lower_colour =='blue' :
  print("You enter a room of Beasts. GAME OVER!")

elif lower_colour == 'yellow' :
  print("You found the Treasure. YOU WIN!")

else :
  print("You chose a door that doesn't exist. GAME OVER!")
