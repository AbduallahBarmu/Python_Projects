import random


def play_game():
    user_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]

    while True:
        user_input = get_user_input(options)

        if user_input == "q":
            print("Final Score:")
            print(f"User: {user_score}")
            print(f"Computer: {computer_score}")
            print("Goodbye!")
            break

        computer_pick = random.choice(options)
        print("Computer Picked:", computer_pick)

        winner = determine_winner(user_input, computer_pick)
        if winner == "user":
            user_score += 1
            print("You won!")
        elif winner == "computer":
            computer_score += 1
            print("You lost!")
        else:
            print("It's a tie!")


def get_user_input(options):
    while True:
        user_input = input("Type Rock, Paper, Scissors, or Quit Game (q): ").lower()
        if user_input == "q" or user_input in options:
            return user_input
        else:
            print("Please enter a valid option or 'q' to quit.")


def determine_winner(user_pick, computer_pick):
    if user_pick == computer_pick:
        return "tie"
    elif (
        (user_pick == "rock" and computer_pick == "scissors")
        or (user_pick == "paper" and computer_pick == "rock")
        or (user_pick == "scissors" and computer_pick == "paper")
    ):
        return "user"
    else:
        return "computer"


if __name__ == "__main__":
    play_game()
