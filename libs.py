def count_words(text: str) -> int:
    return len(text.split())

def count_each_char(text: str) -> dict[str: int]:
    obj = {}
    for char in text:
        item = char.lower()
        if not obj.get(item):
            obj[item] = 1
        else:
            obj[item] = obj[item] + 1
    return obj
