from stats import count_words
from stats import count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_words(book)
    print(f"{count} words found in the document")
    print(count_chars(book))


main()
