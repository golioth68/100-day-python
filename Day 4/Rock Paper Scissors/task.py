import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

ascii_art = {"rock": rock, "paper": paper, "scissors": scissors}
R_P_S = ['rock', 'paper', 'scissors']

name = input("What is your name? ")
shall_we_play = input("Shall we play a game? ").strip().lower()

if shall_we_play == "yes":
    player_choice = input("Let's play! Rock, Paper, or Scissors? Type, rock, paper, or scissors:" "\n").strip().lower()

    if player_choice not in R_P_S:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    else:
        computer_choice = random.choice(R_P_S)

        print(f"\nYou chose:\n{ascii_art[player_choice]}")
        print(f"Computer chose:\n{ascii_art[computer_choice]}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            print( name + "You won!")
        else:
            print( name + " You lost!")
else:
    print("Okay, bye " + name + " !")
