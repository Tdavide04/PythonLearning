def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict1.update(dict2)
    return dict1

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

