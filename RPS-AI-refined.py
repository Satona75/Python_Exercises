#This game plays Rock, Paper, Scissors against the computer

computer_score = 0
player_score = 0
win_score = 2


while computer_score < win_score and player_score < win_score:
    print("Rock...")
    print("Paper...")
    print("Scissors...\n")

    print(f"Computer Score: {computer_score}, Your Score: {player_score}")
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
                player_score += 1
            elif player == "scissors":
                print("Computer Wins!")
                computer_score += 1
        elif computer == "paper":
            if player == "scissors":
                print("You Win!")
                player_score += 1
            elif player == "rock":
                print("Computer Wins!")
                computer_score += 1
        elif computer == "scissors":
            if player == "rock":
                print("You Win!")
                player_score += 1
            elif player == "paper":
                print("Computer Wins!")
                computer_score += 1
        else:
            print("Something has gone wrong!")
    else:
        print("Please enter either rock, paper or scissors")
            

