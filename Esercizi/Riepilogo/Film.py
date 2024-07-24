class Movie:
    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
        else:
            return f"Il film {self.title} è già noleggiato."
        
    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            return f"Il film {self.title} non è attualmente noleggiato."

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movies:list[Movie] = []

    def rent_movie(self, movie: Movie):
        if movie.title not in self.rented_movies:
            self.rented_movies.append(movie)
        else:
            return "Movie is already rented"
    
    def return_movie(self, movie: Movie):
        if movie.title in self.rented_movies:
            self.rented_movies.remove(movie)
        else:
            return "Movie not found"
        
class VideoRentalStore:
    def __init__(self) -> None:
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movies:
            movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie
        else:
            return f"Movie already registered"
        
    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers:
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
        else:
            return "Customer already registerd"
        
    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id not in self.customers:
            return "Customer not found"
        if movie_id not in self.movies:
            return "Movie not found"
        else:
            movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)
            self.movies[movie_id].rent()

    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id not in self.customers:
            return "Customer not found"
        if movie_id not in self.movies:
            return "Movie not found"
        else:
            movie = self.movies[movie_id]
            self.customers[customer_id].return_movie(movie)
            self.movies[movie_id].return_movie()
    
    def get_rented_movies(self,customer_id: str) -> list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            return "Cliente non trovato"
        
# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")