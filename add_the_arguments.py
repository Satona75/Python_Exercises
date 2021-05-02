def addition(*nums):
    total = 0
    for x in nums:
        total += x
    print(total)

addition(*[1,2,3,4,5])
