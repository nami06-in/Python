"""
    WAP that works out whether if a given number is odd or even number 
    HINT: Remainder of any Even number is 0
    
"""

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an Even number.")
else:
    print("This is an Odd number.")