# Input a list of student scores
student_scores = input().split()   # student_scores=[78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
# print(student_scores)
for num1 in student_scores:
  for num2 in student_scores:         # This is too complicated solution. Instead do it as shown in option2
    if num2>num1:
      a=num2

print (f"The highest score in the class is: {a}")

------------------------------------------------------------

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇                     # This is easy and simple solution by comparing a number to newly created big_num.
big_num=0
for score in student_scores:
  if score > big_num:
    big_num=score
print (f"The highest score in the class is: {big_num}")