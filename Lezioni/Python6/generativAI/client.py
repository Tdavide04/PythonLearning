
import requests, json, sys

base_url = "https://127.0.0.1:8080"
sGoogleApiKey = "AIzaSyCEmVkEpyVHfEoKHE4bRIl6t-P4iOW5rto"
api_url = base_url + sGoogleApiKey


print("Benvenuti al Comune - sede locale")

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Inserisci una domanda")
    print("2. Richiedi una domanda su un'immagine")
    print("3. Esci")

    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        sDomanda = input("Inserisci domanda: ")
        jsonDataRequest = {"contests": [{"parts":[{"text":sDomanda}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify=True)
        if response.status_code == 200:
            print(response.json())
            lListaRisposte = response.json()["candidates"]
            for dRisposta in lListaRisposte:
                sTestoRisposta = dRisposta["content"]["parts"][0]["text"]
                print(sTestoRisposta)


    # Richiesta dati cittadino
    elif iOper == 2:
        sImage = input("Inserisci file img da analizzare: ")
        sDomanda = input("Inserisci la domanda: ")

    elif iOper == 3:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")
