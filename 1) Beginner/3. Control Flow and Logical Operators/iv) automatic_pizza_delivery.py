"""
  WAP to build an automatic pizza order, based on a user's order, work out their final bill.
  Reffer pizza_delivery_flowchart.jpg

  Small pizza:$15
  Medium pizza:$20
  Large Pizza:$25

  pepperoni for small pizza: +$2
  pepperoni for medium or large pizza: +$3
  Extra cheese for any size pizza: +$1

"""

# First Method:-
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")



# Second Method:-
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == 'S' :
#   bill = 15  
#   if add_pepperoni == 'Y' :
#     bill += 2    
    
# elif size == 'M' :
#   bill = 20
#   if add_pepperoni == 'Y' :
#     bill += 3
  
# else :
#   bill = 25
#   if add_pepperoni == 'Y' :
#     bill += 3

# if extra_cheese == 'Y' :
#   bill += 1

# print(f"Your final bill is: ${bill}.")



