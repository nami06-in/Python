"""
  WAP which is a virtual coin toss program. It will randomly tells the user "Heads" or "Tails"

  You should generate either 0 or 1 
  1 -> Heads
  0 -> Tails

"""

import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")
