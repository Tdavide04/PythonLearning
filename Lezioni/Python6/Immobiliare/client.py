import sys

import requests
from util import *

print("Benvenuto nella pagina dell'automercato")
accesso = input("Vuoi fare l'accesso? [Y/N] \n").strip()

if accesso.upper() == "Y":
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