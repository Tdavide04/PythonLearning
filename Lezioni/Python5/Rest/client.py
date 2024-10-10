import requests, json, sys
from myjson import start

base_url = "https://127.0.0.1:8080"

def CreateDatiCittadino():
    nome = input("Qual'è il nome? ")
    cognome = input("Qual'è il cognome? ")
    dataN = input("Qual'è la data di nascita? ")
    codF = input("Qual'è il codice fiscale? ")
    """
    {
        "nome": "Mario",
        "cognome":"Retti",
        "data nascita": "22/05/2010",
        "codice fiscale": "dfrcde23t44h501u"
    }
    """
    datiCittadino = {"nome":nome, "cognome": cognome, "data nascita":dataN, "codice fiscale":codF}
    return datiCittadino

def ReadDatiCittadino():
    codF = input("Qual'è il codice fiscale? ")
    codF = {"codice fiscale": codF}
    return codF

def UpdateDatiCittadino():
    nome = input("Qual'è il nome? ")
    cognome = input("Qual'è il cognome ")
    dataN = input("Qual'è la data di nascita? ")
    codF = input("Qual'è il codice fiscale? ")
    datiCittadino = {"nome":nome, "cognome": cognome, "data nascita":dataN, "codice fiscale":codF}
    return datiCittadino

print("Benvenuto")
id = input("id: ")
password = input("password: ")
login_data = {"id" : id, "password" : password}
api_url = base_url + "/login"
try:
    response = requests.post(api_url, json=login_data, verify=False)
    data = response.json()
    if data["Esito"] == "000":
        id_utente = data["id"]
        pwd_utente = data["password"]
        adim = data["admin"]
        print(data)
    else:
        print("User non trovato")
        sys.exit()
except:
    print("Problemi di comunicazione con il server, riprova più tardi")
    sys.exit()

if adim == "true":
    start()
    sOper = input("Cosa vuoi fare?")

    while True:
        if sOper == "1":
            print("Richiesto atto di nascita")
            api_url = base_url + "/add_cittadino"
            jsonDataRequest = CreateDatiCittadino()
            try:
                response = requests.post(api_url,json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                print(data1, data)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")

        if sOper == "2":
            print("Richiesto codice fiscale")
            api_url = base_url + "/read_cittadino"
            jsonDataRequest = ReadDatiCittadino()
            try:
                response = requests.get(api_url,json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                print(data1, data)
            except:
                print("Problemi di comunicazione con il server, riprovapiù tardi")
        
        if sOper == "3":
            print("Richiesto dati aggiornati")
            api_url = base_url + "/update_cittadino"
            jsonDataRequest = UpdateDatiCittadino()
            try:
                response = requests.post(api_url,json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                print(data1, data)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")        

        if sOper == "4":
            print("Richiesto atto di nascita")
            api_url = base_url + "/delete_cittadino"
            jsonDataRequest = ReadDatiCittadino()
            try:
                response = requests.delete(api_url,json=jsonDataRequest, verify=False)
                print(response.json())
                print(response.status_code)
                print(response.headers["Content-Type"])
                data1 = response.json()
                print(data1, data)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")     

        if sOper=="5":
            print("Buona giornata!")
            sys.exit()

        start()
        sOper = input("Cosa vuoi fare?")    