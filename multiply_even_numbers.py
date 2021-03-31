def multiply_even_numbers(list):
    evens = [num for num in list if num%2 == 0]
    holder = 1
    for x in evens:
        holder = holder * x
    return holder

print(multiply_even_numbers([1,2,3,4,5,6,7,8]))