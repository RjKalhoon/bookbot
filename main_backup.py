from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    """Reads and returns the contents of a text file as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    filepath = 'books/frankenstein.txt'  # Make sure this path is correct
    book_text = get_book_text(filepath)
    print("=========== BOOKBOT =============")
    print("Analyzing book found at " + filepath)
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = get_char_counts(book_text)
    sorted_char_list = sort_char_counts(char_counts)
    print("--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()
