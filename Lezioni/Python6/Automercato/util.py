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
    dati = input("Inserisci la marca e opzionalmente il modello separati da una virgola: ").strip()
    if not dati:
        print("Input non valido. Devi inserire almeno la marca.")
        return None
    
    lista = [item.strip() for item in dati.split(",")]  # Elimina tutti gli spazi extra
    marca = lista[0].title 
    if len(lista) > 1 and lista[1].title: # Controlla se il modello è stato inserito
        modello = lista[1]
        dati = {"marca": marca, "modello": modello}
    else:
        dati = {"marca": marca}  
    return dati

def UpdateProduct():
    pass