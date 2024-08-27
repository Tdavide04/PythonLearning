'''
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, somma il valore al valore già associato alla chiave.

For example:

Test	
print(lista_a_dizionario([("a", 1), ("b", 2), ("c", 3)]))
Output: {'a': 1, 'b': 2, 'c': 3}
print(lista_a_dizionario([("a", 1), ("a", 2), ("a", 3)]))
Output: {'a': 6}
'''

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    diz: dict = {}
    for key, value in tuples:
        if key not in diz:
            diz[key] = value
        else:
            diz[key] += value
    return diz

print(lista_a_dizionario([("a", 1), ("b", 2), ("c", 3)]))