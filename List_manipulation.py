def list_manipulation(list,command,location,value=0):
    if (command == 'remove' and location == 'end'):
        print(list.pop())
    elif (command == 'remove' and location == 'beginning'):
        print(list.pop(0))
    elif (command == 'add' and location == 'beginning'):
        print(list.insert(0,value))
    elif (command == 'add' and location == 'end'):
        print(list.insert(len(list),value))

list_manipulation([1,2,3,4],'remove','end')