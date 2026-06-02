import random
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
game_images = [rock, paper, scissors]
user_choice = int(input("Choose your choice: Rock (0), Paper (1) OR Scissors (2): "))
if user_choice >= 0 and user_choice < 3:
    print("You Choose")
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer Choose")
print(game_images[computer_choice])

if user_choice < 0 or user_choice > 2:
    print("You Choose Invalid Number, You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif user_choice < computer_choice:
    print("You Lose!")
elif user_choice == computer_choice:
    print("Its a Draw!")


