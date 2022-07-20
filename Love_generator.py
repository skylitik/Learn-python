
from distutils.command.check import check
from collections import defaultdict
from functools import total_ordering


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name_sum = name1.lower() + name2.lower()
c = ['t','r','u','e']
d = ['l','o','v','e']
count1 = 0
count2 = 0
for key1 in name_sum:
    if str(key1) in c:
        count1 +=1
for key2 in name_sum:
    if str(key2) in d:
        count2 +=1

summary = str(count1) + str(count2)  
total = int(summary)

if total <= 10 or total >=90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
    


