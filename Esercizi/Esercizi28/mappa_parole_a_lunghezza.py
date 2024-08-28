'''
Scrivi una funzione che, data una lista di parole, ritorni un dizionario che mappa ogni parola alla sua lunghezza.
For example:

Test	Result
print(mappa_parole_a_lunghezza(["apple", "banana", "cherry"]))
{'apple': 5, 'banana': 6, 'cherry': 6}
print(mappa_parole_a_lunghezza(["elephant"]))
{'elephant': 8}
'''

def mappa_parole_a_lunghezza(words: list) -> dict:
    diz:dict = {}
    for e in words:
        diz[e] = len(e)
    return diz