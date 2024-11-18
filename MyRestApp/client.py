import requests, sys

base_url = "https://127.0.0.1:8080"

print("Benvenuto")
id = input("id: ")
password = input("password: ")
login_data = {"operator_id" : id, "operatore_password" : password}
api_url = base_url + "/login"
try:
    response = requests.post(api_url, json=login_data, verify=False)
    data = response.json()
    if data.get("Esito") == "200":
        operator_id = data.get("id")
        operator_password = data.get("password")
        operator_access = data.get("access")
        operator_admin = data.get("admin")
        print(data)
    else:
        print("Operator non trovato")
        sys.exit()
    
except:
    print("Problemi di comunicazione con il server, riprova più tardi")
    sys.exit()

def CreateDatiCittadino():
    nome = input("Qual'è il nome? ")
    cognome = input("Qual'è il cognome? ")
    dataNascita = input("Qual'è la data di nascita? ")
    codiceFiscale = input("Qual'è il codice fiscale? ")
    """
    {
        "nome": "Mario",
        "cognome":"Retti",
        "data nascita": "22/05/2010",
        "codice fiscale": "dfrcde23t44h501u"
    }
    """
    datiCittadino = {"nome":nome, "cognome": cognome, "data nascita":dataNascita, "codice fiscale":codiceFiscale}
    return datiCittadino

def ReadDatiCittadino():
    codiceFiscale = input("Qual'è il codice fiscale? ")
    codiceFiscale = {"codice fiscale": codiceFiscale}
    return codiceFiscale

def UpdateDatiCittadino():
    nome = input("Qual'è il nome? ")
    cognome = input("Qual'è il cognome ")
    dataNascita = input("Qual'è la data di nascita? ")
    codiceFiscale = input("Qual'è il codice fiscale? ")
    datiCittadino = {"nome":nome, "cognome": cognome, "data nascita":dataNascita, "codice fiscale":codiceFiscale}
    return datiCittadino

if operator_admin == True and operator_access == True:
    print("Operazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci") 

    comando = input("Scegli un'opzione: ")
    while True:
        if comando == "1":
            print("Richiesto: nome, cognome, data di nascita, codice fiscale")
            api_url = base_url + "/create_cittadino"
            datiCittadino = CreateDatiCittadino()
            try:
                response = requests.post(api_url, json=datiCittadino, verify= False)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
                