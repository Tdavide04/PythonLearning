import requests, sys
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
            print(f"Benvenuto operatore {operator_id}")
        elif response.status_code == 404:
            print(data.get("Msg"))
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
        print("5. Vedi il bilancio")
        print("6. Chiudi la sessione")

        comando = input("Scegli l'operazione: ").strip()
        while True:
            if comando == "1":
                CheckFiliale()
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
                product_data["id"] = id
                product_data["admin"] = operator_admin
                try:
                    response = requests.get(api_url, json=product_data, verify=False)
                    data = response.json()
                    if response.status_code == 200:
                        print("Veicoli trovati con successo!")
                        rows = data.get("veicoli", [])
                        i = 1
                        for row in rows:
                            print(f"Veicolo{i}: {row}")
                            i+= 1
                    elif response.status_code == 404:
                        error = data.get("Msg")
                        print(error)
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            if comando == "3":
                api_url = base_url + "/update_product"
                product_data = UpdateProduct()
                try:
                    response = requests.put(api_url, json=product_data, verify=False)
                    data = response.json()
                    if response.status_code == 200:
                        print(data.get("Msg"))
                    else:
                        print(data.get("Msg"))
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")

            if comando == "4":
                api_url = base_url + "/delete_product"
                product_data = DeleteProduct()
                try:
                    response = requests.delete(api_url, json=product_data, verify=False)
                    data = response.json()
                    if response.status_code == 200:
                        print(data.get("Msg"))
                    else:
                        print(data.get("Msg"))
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")
                    
            if comando == "5":
                api_url = base_url + "/balance"
                balance_data = Balance()
                try:
                    response = requests.get(api_url, json=balance_data, verify=False)
                    data = response.json()
                    if response.status_code == 200:
                        print("Ecco il bilancio:")
                        rows = data.get("vendite", [])
                        i = 1
                        for row in rows:
                            print(f"Vendita{i}: {row}")
                            i+= 1
                        if Serialize(rows):
                            print("Bilancio copiato nel file")
                    elif response.status_code == 404:
                        error = data.get("Msg")
                        print(error)
                except:
                    print("Problemi di comunicazione con il server, riprova più tardi")


            if comando == "6":
                print("Buona giornata!")
                sys.exit()

            print("Operazione disponibili:")
            print("1. Crea prodotto")
            print("2. Visiona prodotto")
            print("3. Modifica prodotto")
            print("4. Elimina prodotto")
            print("5. Vedi il bilancio")
            print("6. Chiudi la sessione")


            comando = input("Scegli l'operazione: ").strip()
            
elif accesso.upper() == "N":

    print("Operazione disponibili:")
    print("1. Visiona prodotto")
    print("2. Esci dal sistema")
    comando = input("Scegli l'operazione: ")
    while True:
        if comando == "1":
            api_url = base_url + "/read_product"
            product_data = ReadProduct()
            try:
                response = requests.get(api_url, json=product_data, verify=False)
                data = response.json()
                if response.status_code == 200:
                    print("Veicoli trovati con successo!")
                    rows = data.get("veicoli", [])
                    i = 1
                    for row in rows:
                        print(f"Veicolo{i}: {row}")
                        i+= 1
                elif response.status_code == 404:
                    error = data.get("Msg")
                    print(error)
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        
        if comando == "2":
            print("Arrivederci!")
            sys.exit()

        print("Operazione disponibili:")
        print("1. Visiona prodotto")
        print("2. Esci dal sistema")
        comando = input("Scegli l'operazione: ").strip()   

else:
    print("Comando non riconosciuto")
    sys.exit()