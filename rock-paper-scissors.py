rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_select = int(input("Choose youre weapon: 1 - Rock, 2 - Paper, 3 - Scissors "))

list_choose =[rock, paper, scissors]
usr_list = list_choose[user_select -1]
print(f"Player: {usr_list}")

comp_choose = random.choice(list_choose)
print(f"Computer: {str(comp_choose)}")

if usr_list == comp_choose:
    print("Deuce")
elif usr_list[2] == comp_choose[1]:
    print("You Won!")
elif usr_list[0] == comp_choose[2]:
    print("You Won!")  
elif usr_list[1] == comp_choose[0]:
    print("You Won!")      
else:
    print("You Loose!")

            