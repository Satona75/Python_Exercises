# Create a function that takes 2 lists as inputs and spits out a new list containing vlaues that are in both input lists

def intersection(a,b):
    return [x for x in a if x in b]

print(intersection([1,2,3,4,5],[0,2,4,8,7,1]))
