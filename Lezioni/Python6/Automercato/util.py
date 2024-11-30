from client import base_url
import requests, sys

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
    marca = input("Marca: ").capitalize()
    modello = input("Modello: ").capitalize()
    prezzo = input("Prezzo: ")
    disponibilita = input("Disponibilita: ")
    filiale_id = input("filiale_id: ")
    dati = {"tipo":tipo, "marca":marca, "modello":modello, "prezzo":prezzo, "disponibilita":disponibilita, "filiale_id":filiale_id}
    return dati

def ReadProduct():
    dati = input("Inserisci la marca e opzionalmente il modello separati da una virgola: ").strip()
    if not dati:
        print("Input non valido. Devi inserire almeno la marca.")
        return None
    lista = [item.strip() for item in dati.split(",")]  # Elimina tutti gli spazi extra
    marca = lista[0].capitalize()
    if len(lista) > 1 and lista[1]: # Controlla se il modello è stato inserito
        modello = lista[1].capitalize()
        dati = {"marca": marca, "modello": modello}
    else:
        dati = {"marca": marca}  
    return dati

def UpdateProduct():
    print("Cosa stai modificando?")
    print("1. Automobile")
    print("2. Motocicletta")
    comando = input()
    if comando == "1":
        tipo = "automobile"
    elif comando == "2":
        tipo = "motocicletta"
    else:
        print("Scelta non valida, riprova.") 
    id = input("id: ")
    marca = input("Marca: ")
    modello = input("Modello: ")
    prezzo = input("Nuovo prezzo: ")
    disponibilita = input("Nuova disponibilita: ")
    filiale_id = input("filiale_id: ")
    dati = {"id":id, "tipo":tipo, "marca":marca, "modello":modello, "prezzo":prezzo, "disponibilita":disponibilita, "filiale_id":filiale_id}
    return dati

def DeleteProduct():
    print("Cosa stai modificando?")
    print("1. Automobile")
    print("2. Motocicletta")
    comando = input()
    if comando == "1":
        tipo = "automobile"
    elif comando == "2":
        tipo = "motocicletta"
    else:
        print("Scelta non valida, riprova.") 
    id = input("id: ")
    marca = input("Marca: ")
    modello = input("Modello: ")
    dati = {"id":id, "tipo":tipo, "marca":marca, "modello":modello}
    return dati

def CheckFiliale():
    while True:
        comando = input("Conosci l'id della filiale in cui inserire il tuo veicolo? [Y/N] \n")
        if comando.upper() == "Y":
            print("Buon lavoro!")
            break
        elif comando.upper() == "N":
            api_url = base_url + "/check_filiale"
            try:
                response = requests.get(api_url, verify=False)
                data = response.json()
                if response.status_code == 200:
                    print("Filiali trovate con successo!")
                    rows = data.get("filiali", [])
                    i = 1
                    for row in rows:
                        print(f"Filiale{i}: {row}")
                        i+= 1
                elif response.status_code == 404:
                    error = data.get("Msg")
                    print(error)
                break
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
                sys.exit()
        else:
            print("comando non valido")