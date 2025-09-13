from libs import count_words, count_each_char

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
"""
Hacer el sort de las key del dict por cantidad de palabras desc
ademas hacer que se vea uno debajo del otro, usar una funcion sort
con un lambda para hacer el filtrado por el value
hacer funcion que reciba el dict, y retorne una lista de dicts

que sea dicts tipo: {"char": "b", "num": 10435}
"""
    print(dict_chars)
    print("============ END ============")

if(__name__ == '__main__'):
    main()
