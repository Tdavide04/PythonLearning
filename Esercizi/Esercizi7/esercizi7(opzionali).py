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
 
# 12. Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
 
# 13. Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
 
# 14. Scrivi una funzione che ritorna un dizionario che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori nel nuovo dizionario.
 
# 15. Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
 
# 16. Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
 
# 17. Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
 
# 18. Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
 
# 19. Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
 
# 20. Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
 
# 21. Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
 
# 22. Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
 
# 23. Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.
 
# 24.  Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
 
# 25. Scrivi una funzione che conta quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato da elementi uguali.
 
# 26. Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

# ESEMPIO: create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)

# OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}

# Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

# ESEMPIO: update_contact(dict, "Mario Rossi", telefono=123456789)

# OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}
