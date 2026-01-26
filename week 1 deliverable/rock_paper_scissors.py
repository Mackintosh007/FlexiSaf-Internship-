import random

def rock_paper_scissors():
    # possible choices
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one: rock, paper, or scissors")

    # input user's choice
    user_choice = input("Your choice: ").lower().strip()

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return

    # Generate computer's choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You win! 🎉")
    else:
        print("Result: Computer wins! 💻")

rock_paper_scissors()
