# Computer generates a random number and the user has to guess it.
# With each wrong guess the computer lets the user know if they are too low or too high
# Once the user guesses the number they win and they have the opportunity to play again

# Random Number generation
from random import randint

carry_on = "y"

while carry_on == "y":
    rand_number = randint(1,10)

    guess = int(input("Try and guess the number generated between 1 and 10 "))

    while guess != rand_number:
        if  guess < rand_number:
            guess = int(input("Sorry too low! Try again.. "))
        else:
            guess = int(input("Sorry too high! Try again.. "))
            
    print("Congratulations!! You have guessed correctly!")
    carry_on = input("Do you wish to play again? (y/n).. ")

print("Thanks for playing!")