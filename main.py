def get_book_text(filepath):
    """Reads and returns the contents of a text file as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # Replace 'frankenstein.txt' with the correct relative path if needed
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    print(book_text)

# Execute the program
if __name__ == "__main__":
    main()