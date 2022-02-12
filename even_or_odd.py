number = int(input("Which number do you want to check? "))

number_odd_even = number % 2

if number_odd_even == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")