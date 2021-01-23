#This program acts as a bouncer at a club
#The rules are:
#If you are under 18 you cannot enter
#If you are over 25 you enter and drink alcohol
#Otherwise you will need a wristband

age = input("What is your age?: ")
if age:
	age = int(age)
	if (age >= 25):
		print("You may enter and drink alcohol")
	elif (age < 18):
		print("You are too young to enter")
	else:
		print("You can enter but must wear a wristband")
else:
	print("Please enter your age")
