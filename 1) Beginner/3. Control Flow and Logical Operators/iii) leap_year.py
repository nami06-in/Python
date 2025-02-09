"""
  WAP that works out whether if a given year is a leap year
  A normal year has 365 days, a leap year has 366 days with an extra day in february.

  HINT: On every year that is evenly divisible by 4, 
        except every year that is evenly divisible by 100,
        unless the year is also evenly divisible by 400.

  Reffer Leap-Year--Flowchart-.jpg

"""

year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")