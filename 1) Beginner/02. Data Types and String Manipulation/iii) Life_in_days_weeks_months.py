"""
    Program using maths and fstring that tells how many days,
    weeks and months we have left, if we live until 90 years old. 

    take age as input
    output must be: You have x days,y weeks, and z months left.
    HINT:
        1 year = 365 days
        1 year= 52 weeks
        1 year = 12 months 
"""

age = int(input("What is your age? "))

years_left = 90 - age
days_left = 365 * years_left
weeks_left = 52 * years_left
months_left = 12 * years_left

print(f"You have {days_left} days left.")
print(f"You have {weeks_left} weeks left.")
print(f"You have {months_left} months left.")