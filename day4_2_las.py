# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
print(names)

names_len = len(names)
names_rand = random.randint(0, names_len)
chart = names[names_rand]
print(f"{chart} is going to buy the meal today!")