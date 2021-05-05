string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
result = {x:len(x) for x in words}
print(result)