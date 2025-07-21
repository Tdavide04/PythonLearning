from datetime import datetime

import requests

base_url = "https://127.0.0.1:8080"

def CercaCasaVendita():
    print("In base a cosa vuoi cercare?\nElenco filtri:")
    print("1. catastale\n2. indirizzo\n3. piano\n4. metri\n5. vani\n6. prezzo\n7. stato")
    filtro = input("Quali opzioni scegli? Puoi usare più di un filtro dividendolo con virgole: ").strip()

    filtro_opzioni = {
        "1": "catastale",
        "2": "indirizzo",
        "3": "piano",
        "4": "metri",
        "5": "vani",
        "6": "prezzo",
        "7": "stato"
    }

    filtri_scelti = [filtro_opzioni.get(f.strip()) for f in filtro.split(",") if f.strip() in filtro_opzioni]

    if not filtri_scelti:
        print("Non hai selezionato filtri validi")
    else:
        print("Hai scelto i seguenti filtri: ")
        for f in filtri_scelti:
            print(f"- {f}")

    dati_filtri = {}
    for filtro in filtri_scelti:
        if filtro == "prezzo":
            try:
                prezzo_min = float(input("Inserisci il prezzo minimo: ").strip())
                prezzo_max = float(input("Inserisci il prezzo massimo: ").strip())
                if prezzo_min > prezzo_max:
                    print("Il prezzo minimo non può essere maggiore del prezzo massimo. Riprova.")
                    prezzo_min = float(input("Inserisci il prezzo minimo: ").strip())
                    prezzo_max = float(input("Inserisci il prezzo massimo: ").strip())
                dati_filtri[filtro] = {"prezzo_min": prezzo_min, "prezzo_max": prezzo_max}
            except ValueError:
                print("Devi inserire un numero valido per il prezzo. Ignorato.")
        else:
            valore = input(f"Inserisci il valore per il filtro '{filtro}': ").strip()
            dati_filtri[filtro] = valore

    print("\nRiepilogo dei filtri scelti e valori:")
    for filtro, valore in dati_filtri.items():
        if filtro == "prezzo":
            print(f"{filtro.capitalize()}: Min {valore['prezzo_min']}, Max {valore['prezzo_max']}")
        else:
            print(f"{filtro.capitalize()}: {valore}")
    
    return dati_filtri


def CercaCasaAffitto():
    print("In base a cosa vuoi cercare?\nElenco filtri:")
    print("1. catastale\n2. indirizzo\n3. tipo_affitto [Totale/Parziale]\n4. bagno_personale [True/False]\n5. prezzo")
    filtro = input("Quali opzioni scegli? Puoi usare più di un filtro dividendolo con virgole: ").strip()

    filtro_opzioni = {
        "0": "nessun filtro",
        "1": "catastale",
        "2": "indirizzo",
        "3": "tipo_affitto",
        "4": "bagno_personale",
        "5": "prezzo",
    }

    filtri_scelti = [filtro_opzioni.get(f.strip()) for f in filtro.split(",") if f.strip() in filtro_opzioni]

    if not filtri_scelti:
        print("Non hai selezionato filtri validi")
    if "0" in filtri_scelti:
        return {}
    else:
        print("Hai scelto i seguenti filtri: ")
        for f in filtri_scelti:
            print(f"- {f}")

    dati_filtri = {}
    for filtro in filtri_scelti:
        if filtro == "prezzo":
            try:
                prezzo_min = float(input("Inserisci il prezzo minimo: ").strip())
                prezzo_max = float(input("Inserisci il prezzo massimo: ").strip())
                if prezzo_min > prezzo_max:
                    print("Il prezzo minimo non può essere maggiore del prezzo massimo. Riprova.")
                    prezzo_min = float(input("Inserisci il prezzo minimo: ").strip())
                    prezzo_max = float(input("Inserisci il prezzo massimo: ").strip())
                dati_filtri[filtro] = {"prezzo_min": prezzo_min, "prezzo_max": prezzo_max}
            except ValueError:
                print("Devi inserire un numero valido per il prezzo. Ignorato.")
        else:
            valore = input(f"Inserisci il valore per il filtro '{filtro}': ").strip()
            dati_filtri[filtro] = valore

    print("\nRiepilogo dei filtri scelti e valori:")
    for filtro, valore in dati_filtri.items():
        if filtro == "prezzo":
            print(f"{filtro.capitalize()}: Min {valore['prezzo_min']}, Max {valore['prezzo_max']}")
        else:
            print(f"{filtro.capitalize()}: {valore}")
    
    return dati_filtri

def VendiCasa():
    print("A quale filiale appartieni?")
    filiale = input("Inserisci filiale: ")
    api_url = base_url + "/check_filiale"
    try:
        response = requests.get(api_url, json={"filiale":filiale}, verify=False)
        if response.status_code == 200:
            pass
        elif response.status_code == 404:
            filiale = None
    except:
        print("Errore di connessione")
        return None
    print("Quale casa vuoi vendere?")
    catastale = input("Inserisci il catastale: ")
    return {"catastale" : catastale, "filiale":filiale}

def AffittaCasa():
    print("A quale filiale appartieni?")
    filiale = input("Inserisci filiale: ")
    api_url = base_url + "/check_filiale"
    try:
        response = requests.get(api_url, json={"filiale":filiale}, verify=False)
        if response.status_code == 200:
            pass
        elif response.status_code == 404:
            filiale = None
    except:
        print("Errore di connessione")
        return None
    print("Quale casa vuoi vendere?")
    catastale = input("Inserisci il catastale: ")
    durata = input("Quanto dura il contratto? ")
    return {"catastale" : catastale, "filiale":filiale, "durata":durata}

def DeleteCasa():
    catastale = input("Quale catastale vuoi eliminare? ")
    return {"catastale":catastale}

