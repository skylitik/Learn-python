import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
names_len = len(names)
names_rand = random.randint(0, names_len -1)
chart = names[names_rand]
print(f"{chart} is going to buy the meal today!")

#chart_pay = random.choice(names)
#print(chart_pay)