def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(f"There are {count_words(text)} words in the given text")
    print(f"the following characters appear in the given text {count_characters(text)}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

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
    



main()