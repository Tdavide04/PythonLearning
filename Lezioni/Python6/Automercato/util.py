def CreateProduct():
    print("Cosa stai creando?")
    print("1. Automobile")
    print("2. Motocicletta")
    comando = input()
    while True:
        if comando == "1":
            tipo = "automobile"
            break
        elif comando == "2":
            tipo = "motocicletta"
            break
        else:
            print("Scelta non valida, riprova.") 

    marca = input("Marca: ")
    modello = input("Modello: ")
    prezzo = input("Prezzo: ")
    disponibilita = input("Disponibilita: ")
    dati = {"tipo":tipo, "marca":marca, "modello":modello, "prezzo":prezzo, "disponibilita":disponibilita}
    return dati
