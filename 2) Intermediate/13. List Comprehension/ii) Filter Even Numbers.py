"""
   WAP to filter out the even numbers from a series of numbers. First, use list comprehension to 
   convert the list_of_strings to a list of integers. 
   Then use list comprehension again to create a new list called result. 
   This new list should only contain the even numbers from the list numbers.

"""

list_of_strings = input("Enter numbers separated by comma: ").split(',')

numbers = [int(x) for x in list_of_strings]

result = [num for num in numbers if num%2==0]

print(result)