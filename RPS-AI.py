#This game plays Rock, Paper, Scissors against the computer
print("Rock...")
print("Paper...")
print("Scissors...\n")

#Player is invited to choose first
player=input("Make your move: ").lower()

#Number is randomly generated between 0 and 2
import random
comp_int=random.randint(0, 2)

if comp_int == 0:
    computer = "rock"
elif comp_int == 1:
    computer = "paper"
else:
    computer = "scissors"

print("Computer has chosen: " + computer)

if player == "rock" or player == "paper" or player == "scissors":
    if computer == player:
        print("It's a tie!")
    elif computer == "rock":
        if player == "paper":
            print("You Win!")
        elif player == "scissors":
            print("Computer Wins!")
    elif computer == "paper":
        if player == "scissors":
            print("You Win!")
        elif player == "rock":
            print("Computer Wins!")
    elif computer == "scissors":
        if player == "rock":
            print("You Win!")
        elif player == "paper":
            print("Computer Wins!")
    else:
        pint("Something has gone wrong!")
else:
    print("Please enter either rock, paper or scissors")
        

