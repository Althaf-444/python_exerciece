import random
from tkinter import *
root = Tk()


def get_choices():

        player_choice = input("Enter your choice (rock, paper, scissors): ")
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        choices = {"player": player_choice, "computer": computer_choice}
        return choices
    
def check_win(player , computer):
    print(f"you chose:{player} | computer chose:{computer}")
    if player== computer:
        return "IT IS A TIE"
    elif ( player == "rock" and computer == "scissors")or\
         (player == "paper" and computer== "rock") or\
         (player == "scissors" and computer == "paper"):
         return "YOU WIN"           
    else :
        return "YOU LOSE"
    
player_point= 0
computer_point=0

for i in range (3):
    choices = get_choices()
    result = check_win(choices["player"],choices["computer"])
    print(f"round {i + 1}:")
    print(result)
    if result== "YOU WIN":
     player_point += 1
    elif result == "YOU LOSE":
     computer_point += 1
    print(f"PLAYER POINT : | {player_point} | ;")
    print(f"COMPUTER POINT: | {computer_point} | ;")
    print("-"* 20)

print("*" * 30)
if player_point > computer_point:
    print("YOU WIN THE GAME!...")
elif player_point < computer_point:
    print("YOU LOSE THE GAME! COMPUTER WINS..")
else:    
    print(" IT IS A TIE..")                
print("*" * 30)

root.mainloop()

