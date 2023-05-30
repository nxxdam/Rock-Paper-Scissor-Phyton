import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock beats scissors! You win! Hell yeah"
    else:
      return "Paper covers rock! You lose. Boo!"
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win! Hell yeah"
    else:
      return "Scissors cuts paper! You lose. Boo!"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win! Yay"
    else:
      return "Rock beats scissors! You lose. Boo!"
      
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)