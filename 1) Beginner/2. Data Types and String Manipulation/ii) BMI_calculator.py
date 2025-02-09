"""
    BMI = weight/(height * height)
    The standard units for calculation is 'Kilogram' for weight and 'meter' for height
    The program can take integer as well as floating numbers
    Output should be integer
    
"""

user_weight = float(input("Enter your weight in kg: "))
user_height = float(input("Enter your height in cm: "))
user_height_in_m = user_height/100 

BMI = int(user_weight / (user_height_in_m ** 2))

print(BMI)