#Pizza order program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

if add_pepperoni == "Y":
    if extra_cheese == "Y":
        if size == "S":
            small_pizza = 18
            print(f"Your final bill is: ${small_pizza}")
        elif size == "M":
            medium_pizza = 24
            print(f"Your final bill is: ${medium_pizza}")
        elif size == "L":
            large_pizza = 29
            print(f"Your final bill is: ${large_pizza}")
    elif extra_cheese == "N":
        if size == "S":
            small_pizza = 17
            print(f"Your final bill is: ${small_pizza}")
        elif size == "M":
            medium_pizza = 23
            print(f"Your final bill is: ${medium_pizza}")
        elif size == "L":
            large_pizza = 28
            print(f"Your final bill is: ${large_pizza}")

if add_pepperoni == "N":
    if extra_cheese == "Y":
        if size == "S":
            small_pizza = 16
            print(f"Your final bill is: ${small_pizza}")
        elif size == "M":
            medium_pizza = 21
            print(f"Your final bill is: ${medium_pizza}")
        elif size == "L":
            large_pizza = 26
            print(f"Your final bill is: ${large_pizza}")
    elif extra_cheese == "N":
        if size == "S":
            small_pizza = 15
            print(f"Your final bill is: ${small_pizza}")
        elif size == "M":
            medium_pizza = 20
            print(f"Your final bill is: ${medium_pizza}")
        elif size == "L":
            large_pizza = 25
            print(f"Your final bill is: ${large_pizza}")