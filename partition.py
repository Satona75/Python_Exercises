def isEven(num):
    return num % 2 == 0

def partition(list, isEven):
    even = [x for x in list if isEven(x)]
    odd = [x for x in list if isEven(x) == False]
    return [even,odd]

print(partition([1,2,3,4], isEven))

# This can be simplified with
# return [[x for x in list if isEven(x)],[x for x in list if isEven(x) == False]]