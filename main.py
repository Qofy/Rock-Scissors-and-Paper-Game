#Ask a question
#the input answers should be between r/s/p
#any other letter should generate error
#make computer choice
#determin who wins
#and terminate it

import random
chioces = ("r", "s", "p")
emoji = {"r": "🗿", "s": "✂", "p":"📜"}
def get_user_choice():
    while True:
         user_choice = input("Rock, Scissors, or Paper (r/s/p): ")
         if user_choice in chioces:
             return user_choice
         else:
            print("Choose between rock, scissors, or paper (r/s/p)")
def display_choice(user_choice, computer_choice):
    print(f"You chose {emoji[user_choice]}")
    print(f"Computer chose {emoji[computer_choice]}")
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif ((user_choice == "r" and computer_choice == "p") or
          (user_choice == "r" and computer_choice == "s") or
          (user_choice == "s" and computer_choice == "p")
    ):
        print("You win 🎉")
    else:
        print("You Loose")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(chioces)
        display_choice(user_choice,computer_choice)
        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            break
play_game()