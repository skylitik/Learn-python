#A Program that calculate the tip for barman and other))

print("Welcome to the tip calculator")
summary = input("What was the total bill? $")
summary_float = float(summary)
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
percent_summary = ((percent / 100) * summary_float)
total_with_tip = summary_float + percent_summary
bil_per_person = total_with_tip / people
result = round(bil_per_person,2)
result = "{:.2f}".format(bil_per_person)
print(f"Each person should pay: ${result}")