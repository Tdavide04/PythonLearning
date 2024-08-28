'''
Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
For example:

Test	
print(filtra_e_mappa({"prodotto1": 30.0, "prodotto2": 60.0, "prodotto3": 45.0}))
Output: {'prodotto1': 33.0, 'prodotto3': 49.5}
print(filtra_e_mappa({"prodotto1": 55.0, "prodotto2": 70.0, "prodotto3": 80.0}))
Output: {}
'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    diz: dict = {}
    for key, value in prodotti.items():
        if value < 50:
            diz[key] = round(value + (value/10), 2)
    return diz

print(filtra_e_mappa({"prodotto1": 30.0, "prodotto2": 60.0, "prodotto3": 45.0}))