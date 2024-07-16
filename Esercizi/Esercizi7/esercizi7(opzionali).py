# 1. Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.

def func1(diz: dict, value: str):
    
    for key, val in diz.items():
        if val == value:
            return key
    return "None"

diz={"1":"ciao", "2":"hello","3":"arancia"}
val="hello"
print(func1(diz, val))

# 2. Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.

def func2(diz):

    diz2 = {}
    for key, val in diz.items():
        diz2[val] = key
    return diz2

print(func2(diz={"1":"ciao", "2":"hello","3":"arancia"}))
 
# 3. Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.

def func3(lista: list, fattore: int):
    lista2 = []
    lista3 = []
    for e in lista:
        if e % 2 == 0:
            lista2.append(e)
    for i in lista2:
        i *= fattore
        lista3.append(i)
    return lista3

print(func3([1,2,3,4,5,6,7], 8))

# 4. Scrivi una funzione che determina se un numero è 'magico'. Un numero è considerato magico se è divisibile per 4 ma non per 6.

def func4(number):
    
    if (number / 4).is_integer():                         #is_integer() è una funzione che deriva dalla classe float
        if (number / 6).is_integer():
            return f"il numero {number} non è magico"
        else:
            return f"Il numero {number} è magico"
    return f"il numero {number} non è magico"

print(func4(36))
 
# 5. Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.

def func5(lista) -> int:

    sumlist = []
    for e in lista:
        if (e / 2).is_integer():
            if (e / 3).is_integer():
                sumlist.append(e)
    return sum(sumlist)

print(func5([1,2,3,4,5,6,7,8,9,10,11,12,15,18]))
 
# 6. Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, 
# scontati del 10%.

def func6(diz):
    diz2 = {}
    for key, val in diz.items():
        if val >= 20:
            new_val = val - ((val / 100) * 10)
            diz2[new_val] = key
    return diz2

prodotti = {
    "Pomodoro": 21.20,
    "Melone": 20.50,
    "Arancia": 0.80,
    "Banana": 0.40,
    "Uva": 15.50
}

print(func6(prodotti))
# 7. Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
 
def func7(voti):

    aggregati = {}
    for voto in voti:
        for studente, nota in voto.items():
            if studente in aggregati:
                aggregati[studente].append(nota)
            else:
                aggregati[studente] = [nota]
    return aggregati

voti = [
    {"Mario": 8, "Gianni": 7},
    {"Mario": 9, "Lorenzo": 6},
    {"Gianni": 8, "Luca": 9}
]

aggregati = func7(voti)
print(aggregati)

# 8. Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
# Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
 
def func8(lista: list, diz: dict):
    
    for key, val in diz.items():
        while val > 0 and key in lista:
            lista.remove(key)
            val -= 1
    return lista

lista = ["ciao", "hello", "ciao", "hola", "hello", "pefforza", "ciao", "ciao"]
diz = {"ciao" : 2, "hola" : 1}

print(func8(lista, diz))

# 9. Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
# Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
 
def func9(lista: list[set]) -> dict:

    diz = {}
    for key, value in lista:
        if key in diz:
            diz[key].append(value)
        else:
            diz[key] = [value]
    return diz

my_list = [
    ("a", 1),
    ("b", 2),
    ("c", 3),
    ("d", 4),
    ("a", 5)
]

print(func9(my_list))

# 10. Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

def func10(lista):

    diz = {"pari":[], "dispari":[]}
    for e in lista:
        if e % 2 == 0:
            diz["pari"].append(e)
        else:
            diz["dispari"].append(e)
    return diz

print(func10([1,2,3,4,5,6,7,8,9,10,11,12,15,18]))
 
# 11. Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro. Utilizza il concetto di parametri opzionali.
 
def func11(temperatura: float) -> float:
    pass    


# 12. Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def func12(lista: list, threshold: int):
    new_list: list = []
    for e in lista:
        if e > threshold:
            new_list.append(e)
    y = sum(new_list)
    return y

print(func12([1,2,3,4,5,6,7,8,9,10,11,12,15,18], 5))

# 13. Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

def func13(lista: list):

    diz: dict = {}
    for e in lista:
        if e in diz:
            diz[e] += 1
        else:
            diz[e] = e
    return diz

print(func13([1,2,3,4,5,4,7,4,9,11,11,12,15,18]))

# 14. Scrivi una funzione che ritorna un dizionario che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori nel nuovo dizionario.

def func14(diz1: dict, diz2: dict):

    for key, value in diz1.items():
        if key in diz2:
            diz2[key] += value
        else:
            diz2[key] = value
    return diz2

diz1 = {"banana" : 3, "mela": 4, "carciofo" : 1}
diz2 = {"banana" : 1, "salame" : 3, "mela" : 3}
print(func14(diz1, diz2))

# 15. Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.

def func15(lista1: list, lista2: list):
    for e in lista2:
        if e in lista1:
            while e in lista1:
                lista1.remove(e)
    return lista1

print(func15(lista1=[1,2,3,4,5,5,6,7], lista2=[2,5,3,9]))

# 16. Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.

def func16(lista: list):
    e_max = max(lista)
    e_min = min(lista)
    e_media = sum(lista) / len(lista)

    return f"il numero massimo della lista è {e_max}, il numero minimo è {e_min} e la media è {e_media}"

print(func16(lista=[1,2,3,4,5,6,6,7,8]))

# 17. Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

def func17(lista: list):

    return round(sum(lista) / len(lista))

print(func17(lista=[1,2,3,4,7,6,6,7,8]))

# 18. Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

def func18(lista: list):

    return list(set(lista))

print(func18(lista=["ciao", 2, 4, 5, 2, 4, "ciao", "come va?"]))

# 19. Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
# La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. 
# Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

def func19(lista: list, k: int):
    
    # if k > len(lista):
    #     k -= len(lista)
    for e in lista:
        lista.index(e) - k
    return lista

print(func19(lista=[1,2,5,6,2,3], k= 2))

# 20. Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
# L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
 
def func20(username: str, password: str, status: str):

    if username == "admin" and password == "12345" and status == "attivo":
        return "Accesso consentito"
    else:
        return "Accesso negato"

print(func20(username="admin", password="12345", status="attivo"))

# 21. Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
# L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
 
def func21(A: bool, B: bool, C: bool):
    if A == True:
        return "Accesso consentito"
    elif B == True and C == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    
print(func21(A=True, B=True, C=False))

# 22. Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.

def func22(number: int):
    
    for e in range(number, 0, -1):
        print(e)

func22(23)

# 23. Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". 
# Un numero magico è definito come un numero che contiene il numero 7.

def func23(number: int):
    
    if "7" in list(str(number)):
        return f"{number} is a magic number"
    else:
        return f"{number} is not a magic number"

print(func23(37))

# 24.  Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
# cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

def func24(stringa: str):

    list(str(stringa))
    for e in stringa:
        if e == "(":
            pass



# 25. Scrivi una funzione che conta quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato da elementi uguali.
 
# 26. Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

# ESEMPIO: create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)

# OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}

# Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

# ESEMPIO: update_contact(dict, "Mario Rossi", telefono=123456789)

# OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}
