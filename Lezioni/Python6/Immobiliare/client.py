import sys

import requests
from util import *

print("Benvenuto nella pagina dell'automercato")
accesso = input("Vuoi fare l'accesso? [Y/N] \n").strip()

if accesso.upper() == "Y":
    id = input("id: ").strip()
    while not id.isdigit():
        print("L'id deve essere un numero intero valido")
        id = input("id: ").strip()
    password = input("password: ").strip()
    while not password.isalpha():
        print("La password deve essere una stringa valida")
        password = input("password: ").strip()
    login_data = {"operator_id" : id, "operator_password" : password}
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
            operator_type = operator.get("tipo")
            print(f"Benvenuto operatore {operator_id}")
        elif response.status_code == 404:
            print(data.get("Msg"))
            sys.exit()
        
    except:
        print("Problemi di comunicazione con il server, riprova più tardi")
        sys.exit()


    if operator_type == "filiale":
        if operator_access == True and operator_admin == True:
            print("Operazione disponibili:")
            print("1. Crea casa\n2. Visiona case\n3. Vendi casa\n4. Elimina prodotto\n5. Chiudi la sessione")
            comando = input("Scegli l'operazione: ").strip()
            while True:
                if comando == "1":
                    pass
                elif comando == "2":
                    print("Quale tipologie di casa stai cercando?")
                    print("1. Case in vendita\n2. Case in affitto")
                    scelta = input()

                    while True:
                        if scelta == "1":
                            api_url = base_url + "/case_in_vendita"
                            dati_ricerca = CercaCasaVendita()
                            try:
                                response = requests.get(api_url, json=dati_ricerca, verify=False)
                                data = response.json()
                                if response.status_code == 200:
                                    print(data.get("Msg"))
                                    rows = data.get("case", [])
                                    i = 1
                                    for row in rows:
                                        print(f"Casa{i}: {row}")
                                        i+= 1
                                elif response.status_code == 404:
                                    error = data.get("Msg")
                                    print(error)
                            
                            except:
                                print("Problemi di comunicazione con il server, riprova più tardi")

                        elif comando == 2:
                            api_url = base_url + "/case_in_affitto"
                            data = CercaCasaAffitto()
                            try:
                                response = requests.get(api_url, json=dati_ricerca, verify=False)
                                data = response.json()
                                if response.status_code == 200:
                                    print(data.get("Msg"))
                                    rows = data.get("case", [])
                                    i = 1
                                    for row in rows:
                                        print(f"Casa{i}: {row}")
                                        i+= 1
                                elif response.status_code == 404:
                                    error = data.get("Msg")
                                    print(error)
                            
                            except:
                                print("Problemi di comunicazione con il server, riprova più tardi")

                        else:
                            print("Comando sbagliato, ritenta")

                elif comando == "3":
                    api_url = base_url + "/vendi_casa"
                    dati_vendita = VendiCasa()
                    try:
                        response = requests.post(api_url, json=dati_vendita, verify=False)
                        data = response.json()
                        if response.status_code == 200:
                            print(data.get("Msg"))
                        elif response.status_code == 404:
                            error = data.get("Msg")
                            print(error)
                    
                    except:
                        print("Problemi di comunicazione con il server, riprova più tardi")

                elif comando == "4":
                    pass

                elif comando == "5":
                    print("Arrivederci")
                    sys.exit()

    elif operator_type == "marketing":
        if operator_access == True:
            pass


elif accesso.upper() == "N":

    print("Operazione disponibili:")
    print("1. Consulta il catalogo\n2. Esci dal sistema")
    comando = input("Quale operazione vuoi fare? ")

    while True:
        if comando == "1":
            print("Quale tipologie di casa stai cercando?")
            print("1. Case in vendita\n2. Case in affitto")
            scelta = input()

            while True:
                if scelta == "1":
                    api_url = base_url + "/case_in_vendita"
                    dati_ricerca = CercaCasaVendita()
                    try:
                        response = requests.get(api_url, json=dati_ricerca, verify=False)
                        data = response.json()
                        if response.status_code == 200:
                            print(data.get("Msg"))
                            rows = data.get("case", [])
                            i = 1
                            for row in rows:
                                print(f"Casa{i}: {row}")
                                i+= 1
                        elif response.status_code == 404:
                            error = data.get("Msg")
                            print(error)
                    
                    except:
                        print("Problemi di comunicazione con il server, riprova più tardi")

                elif comando == 2:
                    api_url = base_url + "/case_in_affitto"
                    data = CercaCasaAffitto()
                    try:
                        response = requests.get(api_url, json=dati_ricerca, verify=False)
                        data = response.json()
                        if response.status_code == 200:
                            print(data.get("Msg"))
                            rows = data.get("case", [])
                            i = 1
                            for row in rows:
                                print(f"Casa{i}: {row}")
                                i+= 1
                        elif response.status_code == 404:
                            error = data.get("Msg")
                            print(error)
                    
                    except:
                        print("Problemi di comunicazione con il server, riprova più tardi")

                else:
                    print("Comando sbagliato, ritenta")
        
        elif comando == "2":
            print("Arrivederci!")
            sys.exit()

        else:
            print("Comando non riconosciuto. Riprova.")
                
else:
    pass