import random
import sys
import time


def computer_choosing():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write(f'\rThe computer is choosing...{animation[i % len(animation)]}')
        sys.stdout.flush()
    print("\rThe computer chose.".ljust(29, " "))

def get_computer_choice():
    computer_choice = ""
    match random.randint(1, 3):
        case 1:
            computer_choice = "rock"
        case 2:
            computer_choice = "paper"
        case 3:
            computer_choice = "scissors"
    return computer_choice

def get_player_choice():
    player_choice = input("Enter your choice: ").lower().strip()
    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input("Wrong input, try again: ").lower().strip()
    return player_choice

def determine_winner(computer_choice, player_choice):

    if computer_choice == player_choice:
        return "tie"
    elif (computer_choice == "rock" and player_choice == "scissors"
            or computer_choice == "paper" and player_choice == "rock"
            or computer_choice == "scissors" and player_choice == "paper"):
        return "computer"
    else:
        return "player"


def main():
    computer_choosing()
    computer = get_computer_choice()
    player = get_player_choice()
    winner = determine_winner(computer, player)

    if winner == "computer":
        print(f'Computer won! ({player} < {computer})')
    elif winner == "player":
        print(f'You won! ({player} > {computer})')
    else:
        print(f'Draw! ({player} = {computer})')

if __name__ == "__main__":
    main()

