# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_student = 0
for i in student_heights:
  sum_student+=1
  
sum_heigh = 0
for x in student_heights:
  sum_heigh += x
   
avarege = sum_heigh / sum_student
print(round(avarege))

#[156 178 165 171 187]