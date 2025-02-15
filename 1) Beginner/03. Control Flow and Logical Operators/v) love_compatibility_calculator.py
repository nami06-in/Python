"""
  WAP that tests the love compatibility between two people 

  Take both people's names and check for the number of times the letters in the word TRUE occurs.
  Then check for the number of times the letters in the word LOVE occurs.
  Then combine these numbers to make a 2 digit number.

  Print the following message for the respective love scores:
    <10  or  >90 - "Your score is x, you go together like coke and mentos"
    between 40 and 50 - "Your score is y, you are alright together"
    All other cases - "Your score is z"

"""

# First Method:-
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_1 = name1.lower()
name_2 = name2.lower()

t_occurs = name_1.count('t') + name_2.count('t')
r_occurs = name_1.count('r') + name_2.count('r')
u_occurs = name_1.count('u') + name_2.count('u')
e_occurs = name_1.count('e') + name_2.count('e')
total_1 = t_occurs + r_occurs + u_occurs + e_occurs

l_occurs = name_1.count('l') + name_2.count('l')
o_occurs = name_1.count('o') + name_2.count('o')
v_occurs = name_1.count('v') + name_2.count('v')
e_occurs = name_1.count('e') + name_2.count('e')
total_2 = l_occurs + o_occurs + v_occurs + e_occurs

love_score = int(str(total_1) + str(total_2))

if love_score <10 or love_score >90 :
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50 :
  print(f"Your score is {love_score}, you are alright together.")
else :
  print(f"Your score is {love_score}.")



# Second Method:-
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_names = name1 + name2
# lower_names = combined_names.lower()

# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))

# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")