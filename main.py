from libs import count_words, count_each_char, to_array_stats

def main():
    path_to_book = "./books/frankenstein.txt"
    with open(path_to_book) as f:
        contents = f.read()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("---------- Word count ----------")

    num_of_words: int = count_words(contents)

    print(f"Found {num_of_words} total words")
    print("------- Character count -------")

    dict_chars = count_each_char(contents)
    arr_stats = to_array_stats(dict_chars)

    for item in arr_stats:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============ END ============")

if(__name__ == '__main__'):
    main()
