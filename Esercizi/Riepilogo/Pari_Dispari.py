def classifica_numeri(lista: int) -> dict[str:list[int]]:
    
    diz = {"pari": [], "dispari":[]}
    for e in lista:
        if e % 2 == 0:
            diz["pari"].append(e)
        else:
            diz["dispari"].append(e)
    return diz
