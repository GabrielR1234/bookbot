def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(text):
    num_words = text.split()
    return len(num_words)

def character_counter(text):
    lowercase = text.lower()
    character_dict = {}
    for char in lowercase:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sorted_list(character_dict):
    sorted_list = []
    for char, count in character_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list

# def main():
  #  file_contents = get_book_text(sys.argv[1])
   # result = word_counter(file_contents)
    # print(f"Found {result} total words")
    # char_results = character_counter(file_contents)
    # sorted_chars = sorted_list(char_results)
    # for item in sorted_chars:
      #  if item["char"].isalpha():
       #     print(f'{item["char"]}: {item["num"]}')

# main()
