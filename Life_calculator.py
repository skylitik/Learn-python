print("Welcome, please input a number")
age = input("What is your current age? ")

days = 365 * (90 - int(age))
weeks = round(days / 7)
month = round(weeks / 52) * 12

print(f"You have {days} days, {weeks} weeks and {month} months left")