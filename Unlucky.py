# This program should satisfy the following conditions:
# for 4 and 13, print "x is unlucky"
# for even numbers, print "x is even"
# for odd numbers, print "x is odd"

for number in range(1,21):
    if number == 4 or number == 13:
        print(f"{number} is unlucky")
    elif number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")