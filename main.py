print("greetings boots")
from stats import count_words
from stats import count_characters
import sys


def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    alpha_list = sort_characters(count_characters(text))
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    for a in alpha_list:
        print(f"{a["character"]}: {a["num"]}")
    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()



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