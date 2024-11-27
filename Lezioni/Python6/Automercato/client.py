import requests, sys
from util import *

base_url = "https://127.0.0.1:8080"

print("Benvenuto nella pagina dell'automercato")
accesso = input("Vuoi fare l'accesso? [Y/N]")

if accesso.upper() == "Y":
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

    if operator_access == True and operator_admin == True:
        print("Operazione disponibili:")
        print("1. Crea prodotto")
        print("2. Visiona prodotto")
        print("3. Modifica prodotto")
        print("4. Elimina prodotto")

        comando = input("Scegli l'operazione: ")
        while True:
            if comando == "1":
                api_url = base_url + "/create_product"
                product_data = CreateProduct()
                try:
                    response = requests.post(api_url, json=product_data, verify=False)
                    if response.status_code == 200:
                        print("Prodotto creato con successo")
                    else:
                        print("Errore di creazione del prodotto")
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            if comando == "2":
                api_url = base_url + "/read_product"
                product_data = ReadProduct()
                try:
                    response = requests.post(api_url, json=product_data, verify=False)
                    if response.status_code == 200:
                        print("Prodotto creato con successo")
                    else:
                        print("Errore di creazione del prodotto")
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            if comando == "3":
                api_url = base_url + "/update_product"
                product_data = UpdateProduct()
                try:
                    response = requests.post(api_url, json=product_data, verify=False)
                    if response.status_code == 200:
                        print("Prodotto creato con successo")
                    else:
                        print("Errore di creazione del prodotto")
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            if comando == "4":
                api_url = base_url + "/delete_product"
                product_data = ReadProduct()
                try:
                    response = requests.post(api_url, json=product_data, verify=False)
                    if response.status_code == 200:
                        print("Prodotto creato con successo")
                    else:
                        print("Errore di creazione del prodotto")
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            if comando == "5":
                print("Buona giornata!")
                sys.exit()

            print("Operazione disponibili:")
            print("1. Crea prodotto")
            print("2. Visiona prodotto")
            print("3. Modifica prodotto")
            print("4. Elimina prodotto")

            comando = input("Scegli l'operazione: ")
            
elif accesso.upper() == "N":
    pass