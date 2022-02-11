print("Welcome, please input a number")
age = input("What is your current age? ")
age_int=int(age)
years_remaining = 90 - age_int
days = years_remaining * 365
weeks = years_remaining * 52
month = years_remaining * 12
result = f"You have {days} days, {weeks} weeks and {month} months left"
print(result)