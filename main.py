import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    """Reads and returns the contents of a text file as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        sys.exit(1)

    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

    char_counts = get_char_counts(book_text)
    sorted_char_list = sort_char_counts(char_counts)

    print("\nCharacter frequency (alphabetical only, sorted by count):")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()
