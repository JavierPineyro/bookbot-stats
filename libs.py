def count_words(text: str) -> int:
    return len(text.split())

def count_each_char(text: str) -> dict[str, int]:
    obj = {}
    for char in text:
        item = char.lower()
        if not obj.get(item):
            obj[item] = 1
        else:
            obj[item] = obj[item] + 1
    return obj

def to_array_stats(obj: dict[str, int]) -> list[dict[str, int | str]]:
    stat_arr = []
    for key, val in obj.items():
        stat_arr.append({"char": key, "num": val})
    stat_arr.sort(reverse=True, key= lambda items: items["num"])
    return stat_arr
