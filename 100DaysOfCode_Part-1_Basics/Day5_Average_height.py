# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
# print(type(student_heights[2]))

n=0
for height in student_heights:
  n+=height
print (f"total height = {n}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(n/len(student_heights))}")
  
  
  