#A Program that calculate the tip for barman and other))

print("Welcome to the tip calculator")
summary = input("What was the total bill? $")
summary_float = float(summary)
percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
percent_summary = ((int(percent) / 100) * summary_float)
total_with_tip = (summary_float + percent_summary) / int(people)
result = round(total_with_tip,2)
print(f"Each person should pay: ${result}")