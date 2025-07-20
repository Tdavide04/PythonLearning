'''
Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

 
 
Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. 
Il programma deve permettere di aggiungere prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.
'''

class Film:

    def __init__(self, titolo_film, durata) -> None:
        self.titolo_film = titolo_film
        self.durata = durata

class Sala:

    def __init__(self) -> None:
        self.spazio = 30
        
    def prenota_posti(self, num_posti):
        if num_posti < self.spazio:
            self.spazio -= num_posti
            print(f"Hai prenotato {num_posti} posti")
        else:
            raise ValueError("Non ci sono abbastanza posti")
        
        return self.spazio
        
    def posti_disponibili(self): 
        return f"Posti disponibili nella sala: {self.spazio}"

class Cinema:

    def __init__(self) -> None:
        self.sale = []
        self.film = []

    def aggiungi_sala(self, sala: Sala):
        self.sale.append(sala)

    def prenota_film(self, film: Film, num_posti):
        sala = Sala()

        if film in self.film:
            if num_posti < sala.spazio:
                sala.prenota_posti(num_posti)
                return f"Registrazione effettuata per il film {film.titolo_film}"
            else:
                raise ValueError("Non ci sono abbastanza posti")
        else:
            raise ValueError (f"Il film {film.titolo_film} non è disponibile")
        
'''
# Creazione di alcuni film
film1 = Film("Interstellar", 180)
film2 = Film("Inception", 150)

# Creazione di alcune sale
sala1 = Sala()
sala2 = Sala()
sala3 = Sala()

# Creazione del cinema
cinema = Cinema()

# Aggiunta delle sale al cinema
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)
cinema.aggiungi_sala(sala3)

# Verifica dei posti disponibili in una sala
print(sala1.posti_disponibili())

# Prenotazione di alcuni posti in una sala
try:
    sala1.prenota_posti(20)
    print(sala1.posti_disponibili())
except ValueError as e:
    print(e)

# Prenotazione di un film
try:
    cinema.prenota_film(film1, 25)
except ValueError as e:
    print(e)

# Aggiunta di un film disponibile
cinema.film.append(film1)

# Prenotazione di un film disponibile
try:
    print(cinema.prenota_film(film1, 25))
except ValueError as e:
    print(e)
'''

class Prodotto:
    
    def __init__(self, nome: str, quantità: int):
        self.nome = nome
        self.quantità = quantità
        
class Magazzino:
    
    def __init__(self) -> None:
        self.magazzino = {}
    
    def __str__(self):
        return f"Prodotto(nome={self.nome}, quantità={self.quantità})"

    def aggiungi_prodotto(self, prodotto: Prodotto):       
        if prodotto.nome in self.magazzino:
            self.magazzino[prodotto.nome].quantità += prodotto.quantità
        else:
            self.magazzino[prodotto.nome] = prodotto
        
    def cerca_prodotto(self, nome):
        return self.magazzino.get(nome, None)

    def verifica_disponibilità(self, nome):
        prodotto = self.cerca_prodotto(nome)
        if prodotto:
            if prodotto.quantità > 0:
                return f"{prodotto.nome} è disponibile con {prodotto.quantità} unità."
            else:
                return f"{prodotto.nome} non è disponibile."
        else:
            return f"{nome} non esiste in magazzino."
    
'''
# Test case
if __name__ == "__main__":
    # Creazione del magazzino
    magazzino = Magazzino()

    # Creazione di prodotti
    prodotto1 = Prodotto("Mela", 100)
    prodotto2 = Prodotto("Banana", 150)
    prodotto3 = Prodotto("Arancia", 0)

    # Aggiunta dei prodotti al magazzino
    magazzino.aggiungi_prodotto(prodotto1)
    magazzino.aggiungi_prodotto(prodotto2)
    magazzino.aggiungi_prodotto(prodotto3)

    # Ricerca di un prodotto
    prodotto_ricercato = magazzino.cerca_prodotto("Mela")
    print(prodotto_ricercato)  # Output: Prodotto(nome=Mela, quantità=100)

    # Verifica disponibilità dei prodotti
    print(magazzino.verifica_disponibilità("Mela"))    # Output: Mela è disponibile con 100 unità.
    print(magazzino.verifica_disponibilità("Banana"))  # Output: Banana è disponibile con 150 unità.
    print(magazzino.verifica_disponibilità("Arancia")) # Output: Arancia non è disponibile.
    print(magazzino.verifica_disponibilità("Pera"))    # Output: Pera non esiste in magazzino.
'''