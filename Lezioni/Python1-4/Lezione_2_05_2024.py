#come transformare ogni valore di una lista in una chiave di un dizionario

lista: list = ["a", "b", "c"]
diz: dict = {}
for elem in lista:
    diz[elem] = 0

print(diz)




"""
#se usato il comando .items vengono rilasciate le chiavi e i valori a coppie di tuple
for key, value in diz.items():       
    print(key, value)

#se usato il comando .keys è possibile accedere alle chiavi di un dizionario
for key in diz.keys():
    print(key)

#se usato il comando .values è possibile accedere ai valori di un dizionario
for value in diz.values():
    print(value)
"""


