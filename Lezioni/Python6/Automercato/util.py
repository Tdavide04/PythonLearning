import requests, sys, json
from datetime import datetime

base_url = "https://127.0.0.1:8080"


def CreateProduct():
    while True:
        print("Cosa stai creando?")
        print("1. Automobile")
        print("2. Motocicletta")
        comando = input().strip()
        if comando == "1":
            tipo = "automobile"
            break
        elif comando == "2":
            tipo = "motocicletta"
            break
        else:
            print("Scelta non valida, riprova") 
    marca = input("Marca: ").capitalize().strip()
    while not marca.isalpha():
        print("La marca deve essere una stringa valida")
        marca = input("Marca: ").capitalize().strip()
    modello = input("Modello: ").capitalize().strip()
    while not modello.isalpha():
        print("Il modello deve essere una stringa valida")
        modello = input("Modello: ").capitalize().strip()
    prezzo = input("Prezzo: ").strip()
    while not prezzo.isdigit() or not prezzo.isdecimal():
        print("Il prezzo deve essere un numero decimale valido")
        prezzo = input("Prezzo: ").strip()
    disponibilita = input("Disponibilità (True/False): ").lower().strip()
    while disponibilita.lower() not in ['true', 'false']:
        print("La disponibilità deve essere un valore booleano")
        disponibilita = input("Disponibilità (True/False): ").lower().strip()
    filiale_id = input("filiale_id: ").strip()
    while not filiale_id.isdigit():
        print("L'id della filiale deve essere un numero decimale valido")
        filiale_id = input("filiale_id: ").strip()
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
    while True:
        print("Cosa stai modificando?")
        print("1. Automobile")
        print("2. Motocicletta")
        comando = input().strip()
        if comando == "1":
            tipo = "automobile"
            break
        elif comando == "2":
            tipo = "motocicletta"
            break
        else:
            print("Scelta non valida, riprova") 
    id = input("id: ").strip()
    while not id.isdigit():
        print("L'id deve essere un numero intero valido")
        id = input("id: ").strip()
    marca = input("Marca: ").capitalize().strip()
    while not marca.isalpha():
        print("La marca deve essere una stringa valida")
        marca = input("Marca: ").capitalize().strip()
    modello = input("Modello: ").capitalize().strip()
    while not modello.isalpha():
        print("Il modello deve essere una stringa valida")
        modello = input("Modello: ").capitalize().strip()
    prezzo = input("Nuovo prezzo: ").strip()
    while not prezzo.isdigit() or not prezzo.isdecimal():
        print("Il prezzo deve essere un numero decimale valido")
        prezzo = input("Nuovo prezzo: ")
    disponibilita = input("Nuova disponibilità (True/False): ").lower().strip()
    while disponibilita.lower() not in ['true', 'false']:
        print("La disponibilità deve essere un valore booleano")
        disponibilita = input("Nuova disponibilità (True/False): ").lower().strip()
    filiale_id = input("filiale_id: ").strip()
    while not filiale_id.isdigit():
        print("L'id della filiale deve essere un numero decimale valido")
        filiale_id = input("filiale_id: ").strip()
    dati = {"id":id, "tipo":tipo, "marca":marca, "modello":modello, "prezzo":prezzo, "disponibilita":disponibilita, "filiale_id":filiale_id}
    return dati

def DeleteProduct():
    while True:
        print("Cosa stai modificando?")
        print("1. Automobile")
        print("2. Motocicletta")
        comando = input().strip()
        if comando == "1":
            tipo = "automobile"
            break
        elif comando == "2":
            tipo = "motocicletta"
            break
        else:
            print("Scelta non valida, riprova") 
    id = input("id: ").strip()
    while not id.isdigit():
        print("L'id deve essere un numero intero valido")
        id = input("id: ").strip()
    marca = input("Marca: ").capitalize().strip()
    while not marca.isalpha():
        print("La marca deve essere una stringa valida")
        marca = input("Marca: ").capitalize().strip()
    modello = input("Modello: ").capitalize().strip()
    while not modello.isalpha():
        print("Il modello deve essere una stringa valida")
        modello = input("Modello: ").capitalize().strip()
    dati = {"id":id, "tipo":tipo, "marca":marca, "modello":modello}
    return dati

def CheckFiliale():
    while True:
        comando = input("Conosci l'id della filiale in cui inserire il tuo veicolo? [Y/N] \n").strip()
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
            
def Balance():
    data_inizio = input("Immetti la data di inizio (YYYY-MM-DD): ") 
    while not is_valid_date(data_inizio):
        print("La data deve essere nel formato seguente: YYYY-MM-DD")       
        data_inizio = input("Immetti la data di inizio (YYYY-MM-DD): ")    
    data_fine = input("Immetti la data di fine (YYYY-MM-DD): ") 
    while not is_valid_date(data_fine):
        print("La data deve essere nel formato seguente: YYYY-MM-DD")       
        data_fine = input("Immetti la data di fine (YYYY-MM-DD): ")
    dati = {"data_inizio":data_inizio, "data_fine":data_fine}
    return dati
        
def is_valid_date(date_string):
    """
    Verifica se una stringa è in formato 'YYYY-MM-DD'.
    
    Args:
        date_string (str): La stringa da verificare.
    
    Returns:
        bool: True se la stringa è valida, False altrimenti.
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def Serialize(data_dict, file_path = "bilancio.json") -> bool:
    try:
        with open(file_path, "w") as file:
            json.dump(data_dict, file)
        return True
    except Exception:
        return False