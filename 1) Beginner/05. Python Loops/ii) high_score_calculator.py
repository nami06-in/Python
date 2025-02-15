"""
   WAP that calculates the highest score from a list of scores
   important: dont use max()

"""

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0 # or -1000
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")