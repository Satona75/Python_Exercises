# This is a game involving 2 participants
# Player 1 goes first and chooses between Rock, Paper or Scissors
# Player 2 then selects
# The game prints who is the winner of if there is a tie

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1 make your selection between rock, paper or scissors: ")
print("***NO CHEATING!***\n" * 20)
player2 = input("Player 2 now make your selection: ")

if (player1 == "rock" or player1 == "paper" or player1 == "scissors") and (player2 == "rock" or player2 == "paper" or player2 == "scissors"):
	if player1 == "rock":
		if player2 == "scissors":
			print("Player 1 wins!")
		elif player2 == "paper":
			print("Player 2 wins!")
		else:
			print("It's a tie!")

	if player1 == "paper":
		if player2 == "rock":
			print("Player 1 wins!")
		elif player2 == "scissors":
			print("Player 2 wins!")
		else:
			print("It's a tie!")

	if player1 == "scissors":
		if player2 == "paper":
			print("Player 1 wins!")
		elif player2 == "rock":
			print("Player 2 wins!")
		else:
			print("It's a tie!")
else:
	print("You have to type in rock, paper or scissors")



