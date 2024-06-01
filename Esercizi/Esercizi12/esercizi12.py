'''

Sistema di Gestione Biblioteca
Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
    Se non ci sono libri disponibili, restituisce un messaggio di errore.

Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
 
 
Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. 
Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. 
    Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
    Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
'''

class Libro:
    def __init__(self) -> None:
        pass

    

class Biblioteca:

    catalogo: dict = {}
    def __init__(self, libro: Libro) -> None:
        pass

    def aggiungi_libro(self):
        pass

    def presta_libro(self):
        pass

    def restituisci_libro(self):
        pass

    def mostra_libri_disponibili(self):
        pass


class MovieCatalog:

    

    def __init__(self) -> None:
        self.catalogo: dict = {}

    def __str__(self) -> str:
        return str(self.catalogo)
    
    def add_movie(self, director_name, movies): #Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.
        if director_name not in self.catalogo:
            self.catalogo[director_name] = [movies]
        else:
            self.catalogo[director_name].append(movies)

    def remove_movie(self, director_name, movie_name): #Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.
        if director_name in self.catalogo and movie_name in self.catalogo[director_name]:
            self.catalogo[director_name].remove(movie_name)
            if not self.catalogo[director_name]:
                del self.catalogo[director_name]
        else:
            raise ValueError(f"The movie {movie_name} is not in the catalog")

    def list_directors(self): #Elenca tutti i registi presenti nel catalogo.
        return list(self.catalogo.keys())

    def get_movies_by_director(self, director_name): #Restituisce tutti i film di un regista specifico.
        if director_name in self.catalogo:
            return(f"Director Name: {director_name}, Movies: {self.catalogo[director_name]}")
        else:
            raise ValueError(f"{director_name} is not in the catalog")

    def search_movies_by_title(self, title):
        found_movies = {}
        for director, movies in self.catalogo.items():
            if title in movies:
                found_movies[director] = title
        
        if found_movies:
            return found_movies
        else:
            raise ValueError(f"'{title}' does not exist in the catalog")
        

catalog = MovieCatalog()
catalog.add_movie('Quentin Tarantino', ['Pulp Fiction', 'Kill Bill'])
catalog.add_movie('Christopher Nolan', 'Inception')
print(catalog)
print(catalog.list_directors())
print(catalog.get_movies_by_director('Christopher Nolan'))
print(catalog.search_movies_by_title('Inception'))