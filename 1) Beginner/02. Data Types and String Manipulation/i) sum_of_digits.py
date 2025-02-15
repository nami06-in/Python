"""
   Q1) Program that adds digits in a 2-digit number
       i.e  35  ->  3+5=8

"""


user_input_number = input("Enter a number: ")
first_digit = user_input_number[0]
second_digit = user_input_number[1]
sum_of_numbers = int(first_digit) + int(second_digit)
print(f"The sum of {first_digit} and {second_digit} is {sum_of_numbers}")

print()

"""
   Q2) Program that adds digits in a 2-digit or more than 2-digit number
       i.e  35  ->  3+5=8
            123 -> 1+2+3=6 

"""   

user_input_number = int(input("Enter a number: "))
temp = user_input_number
sum_of_numbers=0
while temp != 0:
    sum_of_numbers += (temp % 10)
    temp //= 10
print(f"The sum of digits of {user_input_number} is {sum_of_numbers}")

