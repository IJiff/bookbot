def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def count_words(book):
    word_list = book.split()
    count = 0
    for word in word_list:
        count += 1
    return count


def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_words(book)
    print(f"{count} words found in the document")


main()
