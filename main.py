def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    counter = 0
    while a in text:
        if a != " ":
            counter += 1
        print(a)


main()