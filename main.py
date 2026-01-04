import sys
from stats import get_num_words
from stats import get_character_count
from stats import sort_list


print(sys.argv)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    get_num_words()
    get_character_count()
    sort_list()
