def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:

    diz = {}
    for key, val in prodotti.items():
        if prodotti[key] > 20:
            prodotti[key] -= (prodotti[key] * 10) / 100
            diz[key] = prodotti[key]
    return diz


print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))