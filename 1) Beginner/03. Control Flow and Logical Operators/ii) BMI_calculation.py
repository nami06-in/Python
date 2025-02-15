"""
  WAP that interprets the Body Mass Index based on a users's weight and height. (BMI.py)
  <18.5 - underweight
  >18.5 and <25 - normal weight
  >25 and <30 - slightly overweight
  >30 and <35 - obese
  >35 - clinically obese
  BMI=weight/(height *height)

"""

height = float(input("Enter your Height in 'm': "))
weight = int(input("Enter your weight in 'kg': "))

BMI = weight / (height ** 2)

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")

elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")

elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")

elif BMI <35:
  print(f"Your BMI is {BMI}, you are obese.")

else:
  print(f"Your BMI is {BMI}, you are clinically obese.")