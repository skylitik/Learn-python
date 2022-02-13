year = int(input("Which year do you want to check? "))
year_leap_four = (year/4)%1
year_leap_four_hundred = (year/400)%1
year_one_hundred = (year/100)%1
if year_leap_four == 0:
    print("Leap year.")
elif year_leap_four_hundred != 0:
    print("Not leap year.")
elif year_one_hundred != 0:
    print("Not leap year.")
else:
    print("Leap year.")