import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))


if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose!")
else:
    
    print(game[user_choice])

    
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game[computer_choice])

    
    if user_choice == computer_choice:
        print("It's a draw.")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")
