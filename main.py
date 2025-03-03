from stats import count_words
from stats import count_chars
from stats import create_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_words(book)
    print(f"{count} words found in the document")
    char_counts = count_chars(book)
    count_list = create_sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for entry in count_list:
        print(f"{entry["char"]}: {entry["count"]}")
    print("============= END ===============")

main()
