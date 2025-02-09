"""
    take 3 inputs from user: (total bill), (tip percentage) and (number of peaople)
    (total amount to pay) if you are giving tip = (total bill + (total bill * (tip percentage / 100)))
    amount that each person should pay = (total amount to pay) / (number of peaople)

    If the bill was $150.00, split between 5 people, with 12% tip. 
    Each person should pay (150.00 / 5) * 0.12 = 33.60
    Round the result to 2 decimal places.

"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")

print(f"Each person should pay: ${format(bill_per_person,'.2f')}")