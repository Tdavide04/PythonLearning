import requests, sys

base_url = "https://127.0.0.1:8080"

print("Benvenuto")
id = input("id: ")
password = input("password: ")
login_data = {"id" : id, "password" : password}
api_url = base_url + "/login"
try:
    response = requests.post(api_url, json=login_data, verify=False)
    data = response.json()
    if data["Esito"] == "200":
        operator_id = data["id"]
        operator_password = data["password"]
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

