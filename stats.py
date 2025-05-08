def get_num_words(text):
    """Counts and returns the number of words in a string."""
    words = text.split()
    return len(words)

def get_char_counts(text):
    """
    Returns a dictionary of character frequencies.
    Converts all characters to lowercase first.
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_count_dict):
    """
    Converts the char count dictionary to a list of dictionaries and sorts it by count descending.
    Only includes alphabetical characters.
    """
    sorted_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
