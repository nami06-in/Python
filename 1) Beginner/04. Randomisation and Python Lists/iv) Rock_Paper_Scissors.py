'''
Rock -> 0
Paper -> 1
Scissors -> 2

User -> Rock(0)
Comp -> Rock(0)
It's a Draw

User -> Rock(0)
Comp -> Paper(1)
You Loose

User -> Rock(0)
Comp -> Scissors(2)
You Win
--------------------
User -> Paper(1)
Comp -> Rock(0)
You Win

User -> Paper(1)
Comp -> Paper(1)
It's a Draw

User -> Paper(1)
Comp -> Scissors(2)
You Loose
--------------------
User -> Scissors(2)
Comp -> Rock(0)
You Loose

User -> Scissors(2)
Comp -> Paper(1)
You Win

User -> Scissors(2)
Comp -> Scissors(2)
It's a Draw
--------------------
If user choice and computer choice are equal then it's a draw

if user choice > computer choice AND user choice = 0 and computer choice = 2
you win

if computer choice > user choice AND user choice = 2 and computer choice = 0
you loose

if user choice < 0 and >= 3
You typed invalid number, You Loose

'''

import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")