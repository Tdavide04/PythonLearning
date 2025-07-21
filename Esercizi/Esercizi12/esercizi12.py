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

class Book:
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.available = True


class Library:
    
    def __init__(self):
        self.catalog = []

    def add_book(self, book: Book):
        
        if book not in self.catalog:
            self.catalog.append(book)
            return f"Your book {book.title} has been added successfully"
        
        else:
            raise ValueError(f"This book {book.title}, already exist")

    def lend_book(self, book: Book):

        if book.available == True and book in self.catalog:
            self.catalog.remove(book)
            book.available = False
            return f"You borrowed the book {book.title}"
        
        else:
            raise ValueError(f"This book {book.title} does not exist or has already been borrowed")

    def return_book(self, book: Book):
        
        if book.available == False and book not in self.catalog:
            self.catalog.append(book)
            book.available = True
            return f"You have successfully returned the book {book.title}"

        else:
            raise ValueError(f"Something goes wrong")
        
    def show_available_books(self):
        
        book_titles = [book.title for book in self.catalog]
        return f"These are the books in the library: {', '.join(book_titles)}"

'''
library = Library()
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")

print(library.add_book(book1))  # Aggiungi il libro 1 alla libreria
print(library.add_book(book2))  # Aggiungi il libro 2 alla libreria
print(library.show_available_books())
print(library.lend_book(book1))  # Prendi in prestito il libro 1
print(library.return_book(book1))  # Restituisci il libro 1
print(library.show_available_books())
'''


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
        

'''
catalog = MovieCatalog()
catalog.add_movie('Quentin Tarantino', ['Pulp Fiction', 'Kill Bill'])
catalog.add_movie('Christopher Nolan', 'Inception')
print(catalog)
print(catalog.list_directors())
print(catalog.get_movies_by_director('Christopher Nolan'))
print(catalog.search_movies_by_title('Inception'))
'''