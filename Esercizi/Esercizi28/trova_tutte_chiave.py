'''
Scrivi una funzione che prenda un dizionario e un valore, e ritorni una lista con tutte le chiavi che corrispondono a quel valore, o una lista vuota se il valore non è presente.
For example:

Test	Result
print(trova_tutte_chiavi({'a': 1, 'b': 2, 'c': 1}, 1))
['a', 'c']
print(trova_tutte_chiavi({}, 1))
[]
'''

def trova_tutte_chiavi(dizionario: dict[str: int], valore: int) -> str:
    lista: list = []
    for key, value in dizionario.items():
        if value == valore:
            lista.append(key)
    return lista