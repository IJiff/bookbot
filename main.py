import sys
from stats import count_words
from stats import count_chars
from stats import create_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    count = count_words(book)
    print(f"{count} words found in the document")
    char_counts = count_chars(book)
    count_list = create_sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for entry in count_list:
        print(f"{entry["char"]}: {entry["count"]}")
    print("============= END ===============")

main()
