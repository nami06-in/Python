# Switch values stored inside two variables

first_value = input("a: ")
second_value = input("b: ")

temp = first_value
first_value = second_value
second_value = temp

print("\na: "+first_value)
print("b: "+second_value)