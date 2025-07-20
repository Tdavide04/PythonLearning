'''
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, moltiplica i loro valori.
For example:

Test	Result
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  
{'a': 1, 'b': 6, 'c': 4}
print(merge_dictionaries({'x': 5}, {'x': -5}))                 
{'x': -25}
'''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] *= value
        else:
            dict1[key] = value
    return dict1