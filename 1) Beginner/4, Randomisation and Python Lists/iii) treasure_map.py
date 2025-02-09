"""
    write a program that will mark a spot on a map with an X.

    This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
    [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

    ['⬜️', '⬜️', '⬜️']
    ['⬜️', '⬜️', '⬜️']
    ['⬜️', '⬜️', '⬜️']

    First, your program must take the user input and convert it to a usable format.
    Next, you need to use that input to update your nested list with an "X".

    Example Input 1
    B3
    Example Output 1
    Hiding your treasure! X marks the spot.
    ['⬜️', '️⬜️', '️⬜️']
    ['⬜️', '⬜️', '️⬜️']
    ['⬜️️', 'X', '⬜️️']

    Example Input 2
    B1
    Example Output 2
    Hiding your treasure! X marks the spot.
    ['⬜️', 'X', '️⬜️']
    ['⬜️', '⬜️', '️⬜️']
    ['⬜️️', '⬜️️', '⬜️️']

"""


# First Method:-
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ") 

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")




# Second Method:-
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]

# print("Hiding your treasure! X marks the spot.")
# position = input("Where do you want to put the treasure? ") # A1,A2,A3,B1,B2,B3,C1,C2,C3

# row = int(position[1])-1
# col = position[0]
# if col == 'A':
#   column = 0
# elif col == 'B':
#   column = 1
# else:
#   column = 2

# map[row][column] = 'X'

# print(f"{line1}\n{line2}\n{line3}")