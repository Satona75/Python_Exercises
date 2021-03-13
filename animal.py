def speak(animal='dog'):
    if animal == 'pig':
        output =  'oink'
    elif animal == 'duck':
        output = 'quack'
    elif animal == 'cat':
        output = 'meow'
    elif animal == 'dog':
        output = 'woof'
    else:
        output = '?'
    print(output)

speak('pig')

