def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    file_path = "books/frankenstein.txt"
    return get_book_text(file_path)


def get_num_words():
    num_words = main().split()
    print(f"Found {len(num_words)} total words")


def get_character_count():
    force_lowercase = main().lower()
    #    print(force_lowercase)
    character_list = list(force_lowercase)
    #    print(character_list)
    char_count = {}
    for char in character_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_list():
    labeled_char_count = [
        {"char": key_item, "num": value_item}
        for key_item, value_item in get_character_count().items()
    ]
    labeled_char_count.sort(key=lambda chars: chars["num"], reverse=True)
    for items in labeled_char_count:
        print(f"{items['char']}: {items['num']}")
