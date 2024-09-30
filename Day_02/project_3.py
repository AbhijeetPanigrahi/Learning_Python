import random

print("What do you choose? ")

rock = """

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]


outcome_list = [0,1,2]
user_input = int(input("Type 0 for Rock, 1 for paper, 2 for scissors\n"))
print(f"Your input:{game_images[user_input]}")
computer_input = random.choice(outcome_list)
print(f"Computer's input:{game_images[computer_input]}")

if user_input ==  0 and computer_input == 1:
    print("Computer won")
elif user_input ==  0 and computer_input == 2:
    print("You won")
elif user_input ==  1 and computer_input == 0:
    print("You won")
elif user_input ==  1 and computer_input == 2:
    print("Compter won")
elif user_input ==  2 and computer_input == 0:
    print("Compter won")
elif user_input ==  2 and computer_input == 1:
    print("You won")
else:
    print("Match draw")