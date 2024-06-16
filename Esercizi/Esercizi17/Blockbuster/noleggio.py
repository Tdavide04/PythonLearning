from film import Film
from movie_genre import Azione, Commedia, Drama

class Noleggio:
    
    def __init__(self, film_list: list) -> None:
        self.film_list = film_list
        self.rented_film = {}
        
    def isAvaible(self, film: Film) -> bool:
        '''
        tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario. 
        Se il film è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!". 
        Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!".
        '''
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
            
    def rentAMovie(self, film: Film, clientID: int): 
        '''
        tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. 
        Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto, il metodo deve verificare la disponibilità. 
        Nel caso in cui il film richiesto sia disponibile, rimuoverlo dalla lista dei film disponibili in negozio, 
        poi riempire il dizionario rented_film in questo modo:
            la chiave sarà l'id del cliente che noleggia (id_client)
            il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
        '''
        if self.isAvaible(film):
            self.film_list.remove(film)
            if clientID not in self.rented_film:
                self.rented_film[clientID] = []
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")
        
    def giveBack(self, film: Film, clientID: int, days: int):
        '''
        questo metodo consente di restituire un film noleggiato in negozio, ed ha come argomenti il film da restituire, 
        il codice ID del client che restituisce il film, il numero dei giorni in cui il cliente ha tenuto il film per se.  
        Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, 
        deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). 
        Successivamente, il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. 
        Stampare la penale che il cliente deve pagare: "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".
        '''
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            penale = film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale} euro!")
        else:
            print(f"Il cliente {clientID} non ha noleggiato il film {film.getTitle()}!")
        
    def printMovies(self):
        #stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: "{titolo_film} - {genere_film} -"
        print("film disponibili:")
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenere()} -")
            
    def printRentMovies(self, clientID):
        #questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.
        if clientID in self.rented_film:
            for film in self.rented_film[clientID]:
                print(f"{film.getTitle()} - {film.getGenere()} -")
        else:
            print(f"Il cliente {clientID} non ha noleggiato nessun film.")
        
        
if __name__ == "__main__":
    film1 = Azione(1, "Mission Impossible")
    film2 = Commedia(2, "Via Col Vento")
    film3 = Drama(3, "Sherlock Holmes")
    film4 = Azione(4, "Deadpool")
    film5 = Commedia(5, "Benvenuti al Suf")
    film_list = [film1, film2, film3, film4, film5]
    noleggio = Noleggio(film_list)
    noleggio.printMovies()
    noleggio.rentAMovie(film1, 23)
    noleggio.rentAMovie(film1, 12)
    noleggio.rentAMovie(film2, 23)
    noleggio.printMovies()
    noleggio.printRentMovies(23)
    noleggio.giveBack(film1, 23, 5)