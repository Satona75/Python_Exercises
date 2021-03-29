# '''
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True
# '''

def is_palindrome(phrase):
    phrase = phrase.replace(" ","")
    phrase = phrase.lower()
    if phrase == phrase[::-1]:
        print('True')
    else:
        print('False')

is_palindrome('amana Plan a canaL panama')