msg = input("what's the secret password? ")
while msg != "bananas":
    print("WRONG!")
    msg = input("Guess again! What's the secret password? ")
print("CORRECT!")