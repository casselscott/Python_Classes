# rock_paper_scissors.py

import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Enter your choice: 'rock', 'paper', 'scissors' or 'quit' to end the game.")
    
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    
    while True:
        player_choice = input("\nEnter your choice: ").lower()
        
        if player_choice == 'quit':
            print("\nGame ended. Final Scores:")
            print(f"Player: {player_score}  Computer: {computer_score}")
            break
        
        if player_choice not in choices:
            print("Invalid choice! Please enter 'rock', 'paper', 'scissors' or 'quit'.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print(f"Scores - Player: {player_score}  Computer: {computer_score}")

if __name__ == "__main__":
    rock_paper_scissors()
