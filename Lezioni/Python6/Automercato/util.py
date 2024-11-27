def CreateProduct():
    print("Cosa stai creando?")
    print("1. Automobile")
    print("2. Motocicletta")
    comando = input()
    
    if comando == "1":
        tipo = "automobile"
    elif comando == "2":
        tipo = "motocicletta"
    else:
        print("Scelta non valida, riprova.") 

    marca = input("Marca: ")
    modello = input("Modello: ")
    prezzo = input("Prezzo: ")
    disponibilita = input("Disponibilita: ")
    targa = input("Targa: ")
    dati = {"tipo":tipo, "marca":marca, "modello":modello, "prezzo":prezzo, "disponibilita":disponibilita, "targa":targa}
    return dati

def ReadProduct():
    targa = input("Inserisci la marca del prodotto: ")
    dati = {"targa":targa}
    return dati

def UpdateProduct():
    pass