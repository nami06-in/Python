"""
   WAP that calculates the sum of all the even numbers from 1 to X.
   If X is 100 then the first even number would be 2 and the last one is 100
   hint: use range()

"""

# First Method:-
target = int(input()) # Number between 0 and 1000

even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)


# Second Method:-
# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number