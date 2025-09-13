from libs import count_words

def main():
    path_to_book = "./books/frankenstein.txt"
    with open(path_to_book) as f:
        contents = f.read()
    num_of_words: int = count_words(contents)
    print(f"{num_of_words} words found in the doc")

if(__name__ == '__main__'):
    main()
