def dict_unpack(first,second):
    return f'{first} is married to {second}'

dictionary = {'first':'Nicholas','second':'Zsuzsanna'}

print(dict_unpack(**dictionary))
