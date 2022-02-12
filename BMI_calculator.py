#A program that calculates the Body Mass Index (BMI) from a user's weight and height.

print("Welcome to a program, let's start!")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / (height ** 2)
bmi_as_int = round(bmi)
if bmi_as_int < 18.5:
    print(f"Your BMI is {bmi_as_int}, you are underweight.")
elif 25 > bmi_as_int:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif 30 > bmi_as_int:
    print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
elif 35 > bmi_as_int:
    print(f"Your BMI is {bmi_as_int}, you are obese.")
else:
    print(f"You BMI is {bmi_as_int}, you are clinically obese.")