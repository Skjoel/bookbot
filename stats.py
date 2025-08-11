def count_words(text):
    words = text.split()
    return len(words)
    
def count_characters(text):
    lowered_string = text.lower()
    alphabet = {}
    for a in lowered_string:
        if a in alphabet:
            alphabet[a] += 1
        else:
            alphabet[a] = 1
    return alphabet

    