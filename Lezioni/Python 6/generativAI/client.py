
import requests, json, sys

base_url = "https://127.0.0.1:8080"
sGoogleApiKey = "AIzaSyCEmVkEpyVHfEoKHE4bRIl6t-P4iOW5rto"


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

    # Richiesta dati cittadino
    elif iOper == 2:
        print("Richiesta dati cittadino")

    elif iOper == 3:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")
