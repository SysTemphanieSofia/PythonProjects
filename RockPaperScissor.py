import random

ascii_art = ['''    
      _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''',
''' _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''',
'''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''']

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer = random.randint(0,2)

if player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:
    print(f"Player Chose {ascii_art[player]}")
    print(f"Computer Chose {ascii_art[computer]}")
    print("You won!")
elif player == 0 and computer == 0 or player == 1 and computer == 1 or player == 2 and computer == 2:
    print(f"Player Chose {ascii_art[player]}")
    print(f"Computer Chose {ascii_art[computer]}")
    print("Its a tie!")
else:
    print(f"Player Chose {ascii_art[player]}")
    print(f"Computer Chose {ascii_art[computer]}")
    print("You lost!")