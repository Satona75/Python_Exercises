def combine_words(word,**order):
    if 'prefix' in order:
        return f"{order['prefix']}{word}"
    if 'suffix' in order:
        return f"{word}{order['suffix']}"
    return word

print(combine_words("child",prefix="man"))
