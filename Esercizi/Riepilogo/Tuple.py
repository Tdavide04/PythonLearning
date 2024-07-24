def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:

    diz: dict = {}
    for key, value in tuples:
        if key in diz:
            diz[key].append(value)
        else:
            diz[key] = [value]
    return diz

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([]))