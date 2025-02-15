"""
    WAP that will select a random name from a list of names.
    The person selected will have to pay for everybody's food bill.

    user must input name like this -> Ann, Ben, Jenny, Michael, Chloe
    Remember that you should add space after each commas.

    important: choice() is not allowed
    hint: len() is allowed

"""

import random

names = input().split(", ") # input name like this -> Ann, Ben, Jenny, Michael, Chloe

# Get the total number of items in list.
num_items = len(names)

# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]
# Choose and print a random name.
print(person_who_will_pay+ " is going to buy the meal today!")