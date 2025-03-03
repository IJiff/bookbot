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


def create_sorted_list(counts):
    letter_list = []
    for c in counts:
        if c.isalpha():
            letter_list.append({"char": c, "count": counts[c]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list


def sort_on(dict):
    return dict["count"]
