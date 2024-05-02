#Q1: Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.

def countdown(n: int) -> int:
    lista: list = []
    for numbers in range(n +1):
        lista.append(numbers)
    lista.reverse()
    for element in lista:
        print(element)
    return lista

#Q2: Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
#La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e 
#l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il 
#numero specificato di posizioni sia maggiore della lunghezza della lista.

#Q3: Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
#L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
#La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA:
        return "Operazione permessa"
    elif conditionB and conditionC:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
#Q4: Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

def frequency_dict(elements: list) -> dict:
    diz: dict = {}
    for elem in elements:
        if elem in diz:
            diz[elem] += 1
        else:
            diz[elem] = 1
    return diz

#Q5: La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
#Un errore nell'implementazione porta a risultati inaspettati.

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)

#Q6: La funzione dovrebbe determinare se un elemento è presente in una lista.
#Un errore nell'implementazione porta a risultati inaspettati.

def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
    return False

#Q7: Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
#cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:
    count = 0
    for elem in expression:
        if elem == "(":
            count += 1
        if elem == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

#Q8: Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
#Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(n) -> int:
    count = 0
    if n == []:
        return count
    else:
        
        if n[0] != n[1]:
            count += 1
        for number in range(1, len(n) -1):
            if n[number] != n[number + 1] and n[number] != n[number - 1]:
                count += 1
        if n[-1] != n[-2]:
            count += 1
        return count
    
#Q9: Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
#ritorni un nuovo insieme senza i numeri specificati nella lista.


#Q10: Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.