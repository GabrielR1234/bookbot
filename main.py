import sys
from stats import get_book_text, word_counter, character_counter, sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_contents = get_book_text(sys.argv[1])
char_results = character_counter(file_contents)
sorted_chars = sorted_list(char_results)

for item in sorted_chars:
    if item["char"].isalpha():
        print(f'{item["char"]}: {item["num"]}')
