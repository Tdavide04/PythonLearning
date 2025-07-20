'''
Dato un file json contenente la stringa seguente:
{ "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}
 
fare le seguenti procedure:
 
def Serialize(dict, file_path)->true/false
def Deserialize(file_path)->dict oppure null
'''

import json

def Serialize(data_dict, file_path = "Lezioni/Python5/json serialize deserialize Completion requirements/file.json") -> bool:
    try:
        with open(file_path, "w") as file:
            json.dump(data_dict, file)
        return True
    except Exception:
        return False

def Deserialize(file_path = "Lezioni/Python5/json serialize deserialize Completion requirements/file.json") -> dict|None:
    try:
        with open(file_path, "r") as file:
            data_dict = json.load(file)
        return data_dict
    except Exception:
        return None