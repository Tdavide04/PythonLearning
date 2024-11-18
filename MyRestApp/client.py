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
        operator = data.get("operator", {})
        operator_id = operator.get("id")
        operator_password = operator.get("password")
        operator_access = operator.get("access")
        operator_admin = operator.get("admin")
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

if operator_access == True and operator_admin == True:
    print("Operazioni disponibili:")
    print("1. Crea cittadino")
    print("2. Visiona cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci") 

    comando = input("Scegli un'opzione: ")
    while True:
        if comando == "1":
            api_url = base_url + "/create_cittadino"
            datiCittadino = CreateDatiCittadino()
            try:
                response = requests.post(api_url, json=datiCittadino, verify= False)
                if response.status_code == 200:
                    print("Cittadino creato con successo")
                else:
                    print("Qualcosa è andato storto")
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        
        if comando == "2":
            api_url = base_url + "/read_cittadino"
            datiCittadino = ReadDatiCittadino()
            try:
                response = requests.get(api_url, json=datiCittadino, verify= False)
                if response.status_code == 200:
                    datiCittadino = response.json()
                    print(datiCittadino["Dati cittadino"])
                else:
                    print("Qualcosa è andato storto")
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")

        if comando == "3":
            api_url = base_url + "/update_cittadino"
            datiCittadino = UpdateDatiCittadino()
            try:
                response = requests.put(api_url, json=datiCittadino, verify= False)
                if response.status_code == 200:
                    print("Dati cittadino modificati con successo")
                else:
                    print("Qualcosa è andato storto")
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")

        if comando == "4":
            pass


        if comando == "5":
            print("Buona giornata!")
            sys.exit()

        print("Operazioni disponibili:")
        print("1. Inserisci cittadino")
        print("2. Richiedi cittadino")
        print("3. Modifica cittadino")
        print("4. Elimina cittadino")
        print("5. Esci") 

        comando = input("Scegli un'opzione: ")


else:
    print("Accesso negato") 