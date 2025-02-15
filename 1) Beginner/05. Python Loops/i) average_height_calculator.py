"""
  WAP that calculates the average student height from a list of heights
  important dont use sum() or len()

"""

# First Method:-
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")


# Second Method:-
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# sum_of_height = 0
# num_of_students = 0

# for i in student_heights:
#   sum_of_height += i
#   num_of_students += 1

# average = sum_of_height/num_of_students
# print(f"total height = {sum_of_height} \nnumber of students = {num_of_students} \naverage height = {round(average)}")