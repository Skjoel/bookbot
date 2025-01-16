def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    alpha_list = sort_characters(count_characters(text))
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    for a in alpha_list:
        print(f"The {a["character"]} character was found {a["num"]} times")
    print(f"--- End report ---")

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

def sort_on(dict):
    return dict["num"]

def sort_characters(dict):
    alphabet_list = []
    for a in dict:
        if a.isalpha():
            alphabet_list.append({"character": a,"num": dict[a]})
    alphabet_list.sort(reverse=True, key=sort_on)
    return alphabet_list




main()