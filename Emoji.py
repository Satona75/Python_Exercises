# For loop String multiplication version
#for num in range (1,11):
#    print("\U0001f600" * num)

# While loop string multiplication version
#num = 1
#while num <= 10:
#    print("\U0001f600" * num)
#    num += 1

#Combination of for and while loop in place of string multiplication
#for num in range(1,11):
    # count = 1
    # smileys = ""
    # while count <= num:
    #     smileys +="\U0001f600"
    #     count += 1
    # print(smileys)

#Creating a centered triangle of emojis
for num in range (1,21,2):
    print((" " *(20 - num)) + ("\U0001f600" * num))



