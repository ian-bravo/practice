import random


def get_choice():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print (f"You chose {player} and computer chose {computer}")
  if player == computer:
    return ("It's a tie!")
  elif player == "rock":
    if computer == "scissors":
      return ("Rock beats scissors, you win!")
    else:
      return ("paper beats rock, you lose ):")
  elif player == "paper":
    if computer == "rock":
      return ("paper beats rock, you win!")
    else:
      return ("scissors beat paper, you lose ):")
  elif player == "scissors":
    if computer == "paper":
      return ("scissors beats paper, you win!")
    else:
      return ("rock beats scissors, you lose ):")

choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)
