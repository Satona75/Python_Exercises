# This function accepts a list and returns a list of vlaues that are truthy, without any falsey values

def compact(list):
    return [x for x in list if x]

print(compact([0,True,2,3,4,5]))