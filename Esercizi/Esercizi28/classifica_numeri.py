'''
Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che classifichi i numeri in liste separate per numeri positivi e negativi.

For example:

Test	Result
print(classifica_numeri([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))
Output: {'positivi': [1, 3, 5, 7, 9], 'negativi': [-2, -4, -6, -8, -10]}
print(classifica_numeri([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
Output: {'positivi': [], 'negativi': [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]}
'''

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    diz: dict = {"positivi":[],"negativi":[]}
    for e in lista:
        if e < 0:
            diz["negativi"].append(e)
        else:
            diz["positivi"].append(e)
    return diz

print(classifica_numeri([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))