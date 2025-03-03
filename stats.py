def count_words(book):
    word_list = book.split()
    count = 0
    for word in word_list:
        count += 1
    return count


def count_chars(book):
    char_counts = {}
    for c in book:
        c = c.lower()
        if c not in char_counts:
            char_counts[c] = 0
        char_counts[c] += 1
    return char_counts
