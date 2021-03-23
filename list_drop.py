def last_element(a):
    if a:   
        return a.pop()
    else:
        return None

print(last_element([1,2,3,4]))
