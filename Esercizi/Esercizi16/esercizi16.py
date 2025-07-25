#Obiettivo:
#Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. 
# Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

#Specifiche della Classe Media:
 
#Attributi:
#- title (stringa): Il titolo del media.
#- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.

#Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, 
# ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, 
# "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, 
# co,il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
#Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello 
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%
# 
# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, 
# aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().

class Media:
    
    def __init__(self, title) -> None:
        self.title: str = title
        self.review: list[int] = []

    def set_title(self, title: str): # Imposta il titolo del media.
        self.title = title

    def get_title(self): # Restituisce il titolo del media.
        return self.title
    
    def aggiungiValutazione(self, voto: int): # Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
        if 1 <= voto <= 5:
            self.review.append(voto)
        else:
            raise ValueError("Error value for a review. It have to be 5 or inferior")
        
    def getMedia(self) -> float: #Calcola e restituisce la media delle valutazioni.
        if not self.review:
            return 0
        return sum(self.review) / len(self.review)
    
    def getRate(self): 
        '''Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1, 
        "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, 
        "Grandioso" se il voto medio si avvicina a 5.
        '''

        media = self.getMedia()
        if round(media) == 1:
            return "Terribile"
        if round(media) == 2:
            return "Brutto"
        if round(media) == 3:
            return "Normale"
        if round(media) == 4:
            return "Bello"
        if round(media) == 5:
            return "Grandioso"
        
    def getRateString(self, voto):
        rate_dict = {
            1: "Terribile",
            2: "Brutto",
            3: "Normale",
            4: "Bello",
            5: "Grandioso"
        }
        return rate_dict.get(voto, "")

    def ratePercentage(self, voto): #Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
        if not self.review:
            return 0
        return (self.review.count(voto))/len(self.review) * 100

    def recensione(self):
        print(f"Titolo: {self.get_title()}")
        print(f"Voto Medio: {self.getMedia()}")
        print(f"Giudizio: {self.getRate()}")        
        for i in range(1, 6):
            print(f"{self.getRateString(i)}: {self.ratePercentage(i)}")


class Film(Media):
    
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director
        
        
'''
# Creare due oggetti Film
film1 = Film("The Shawshank Redemption", "Frank Darabont")
film2 = Film("Inception", "Christopher Nolan")

# Aggiungere valutazioni al primo film
valutazioni_film1 = [5, 4, 3, 5, 4, 2, 5, 1, 3, 4]
for voto in valutazioni_film1:
    film1.aggiungiValutazione(voto)

# Aggiungere valutazioni al secondo film
valutazioni_film2 = [5, 5, 4, 4, 4, 5, 3, 3, 4, 5]
for voto in valutazioni_film2:
    film2.aggiungiValutazione(voto)

# Richiamare il metodo recensione per entrambi i film
film1.recensione()
print("\n")
film2.recensione()
'''


#Esercitazione Classi ed Ereditarietà

'''
Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. La classe offre un modo semplice per tenere traccia di un conteggio 
che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio.

Example: 
c = Contatore()  
c.add1() 
c.mostra()
Reuslt:
Conteggio attuale: 1
'''

class Contatore:
    
    def __init__(self): # Inizializza l'attributo conteggio a 0.
        self.conteggio = 0
    
    def setZero(self): #Imposta il conteggio a 0.
        self.conteggio = 0
        return self.conteggio
    
    def add1(self): #Incrementa il conteggio di 1.
        self.conteggio += 1
        return self.conteggio
    
    def sub1(self): #Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
        if self.conteggio <= 0:
            self.conteggio = 0
            print("Non è possibile eseguire la sottrazione")
        if self.conteggio > 0:
            self.conteggio -= 1
        
        return self.conteggio
    
    def get(self): #Restituisce il valore corrente del conteggio.
        return self.conteggio
    
    def mostra(self): #Stampa a schermo il valore corrente del conteggio.
        print(f"Conteggio attuale: {self.conteggio}")
        
'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. 
Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.
    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
    Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. 
    Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - list_recipes(): Elenca tutte le ricette esistenti.
    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
    Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
    
Example: 
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
Result:
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
{'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']
'''

class RecipeManager:
    
    def __init__(self) -> None:
        self.recipe:dict = {}
    
    def create_recipe(self, name: str, ingredients: list[str]): 
        '''
        Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
        Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
        '''
        
        if name not in self.recipe:
            self.recipe[name] = ingredients
        else:
            raise ValueError(f"The Recipe {name}: {ingredients} already exist")
        return self.recipe
            
    def add_ingredient(self, recipe_name, ingredient): 
        '''
        Aggiunge un ingrediente alla ricetta specificata. 
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
        '''
        if recipe_name in self.recipe:
            if ingredient not in self.recipe[recipe_name]:
                self.recipe[recipe_name].append(ingredient)
            else: 
                raise ValueError(f"The ingredient: {ingredient} already exist")
        else:
            raise ValueError(f"This recipe: {recipe_name} does not exit")
        return self.recipe
    
    def remove_ingredient(self, recipe_name, ingredient): 
        '''
        Rimuove un ingrediente dalla ricetta specificata. 
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
        '''
        if recipe_name in self.recipe:
            if ingredient in self.recipe[recipe_name]:
                self.recipe[recipe_name].remove(ingredient)
            else: 
                raise ValueError(f"The ingredient: {ingredient} does not exist")
        else:
            raise ValueError(f"This recipe: {recipe_name} does not exit")
        return self.recipe
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient): 
        '''
        Sostituisce un ingrediente con un altro nella ricetta specificata. 
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
        '''
        if recipe_name in self.recipe:    
            if old_ingredient in self.recipe[recipe_name]:
                if new_ingredient not in self.recipe[recipe_name]:
                    index = self.recipe[recipe_name].index(old_ingredient)
                    self.recipe[recipe_name][index] = new_ingredient
                else: 
                    raise ValueError(f"The ingredient: {new_ingredient} already exist in this recipe")
            else:
                raise ValueError(f"The ingredient: {old_ingredient} does not exist")
        else:
            raise ValueError(f"This recipe: {recipe_name} does not exit")
        return self.recipe
    
    def list_recipes(self): #Elenca tutte le ricette esistenti.
        
        return list(self.recipe.keys())
    
    def list_ingredients(self, recipe_name): 
        '''
        Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
        '''
        if recipe_name in self.recipe:
            return self.recipe[recipe_name]
        else:
            raise ValueError(f"This recipe: {recipe_name} does not exist")
    
    def search_recipe_by_ingredient(self, ingredient):
        '''
        Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
        Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
        '''
        found_recipes = {}
        for recipe_name, ingredients in self.recipe.items():
            if ingredient in ingredients:
                found_recipes[recipe_name] = ingredients
        
        if found_recipes:
            return found_recipes
        else:
            raise ValueError(f"'{ingredient}' does not exist in any recipe")
        
'''
In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:

    marca (stringa)
    modello (stringa)
    anno (intero)

Metodi:

    __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
    descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:

    numero_porte (intero)

Metodi:

    __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il numero di porte nella descrizione, 
    nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:

    tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

Metodi:

    __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
    descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, 
    nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".

Example: 
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo() 
auto.descrivi_veicolo()
moto.descrivi_veicolo()

Result:
Marca: Generic, Modello: Model, Anno: 2020
Marca: Toyota, Modello: Corolla, Anno: 2021, Numero di porte: 4
Marca: Yamaha, Modello: R1, Anno: 2022, Tipo: sportiva
'''

class Veicolo:

    def __init__(self, marca: str, modello: str, anno: int): #metodo costruttore che inizializza gli attributi marca, modello e anno.
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi_veicolo(self): #metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
    
class Auto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int): #metodo costruttore che inizializza gli attributi della classe base e numero_porte.
        super().__init__(marca, modello, anno)
        self.numero_porte =numero_porte

    def descrivi_veicolo(self): 
        '''
        metodo che sovrascrive quello della classe base per includere anche il numero di porte nella descrizione, 
        nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".
        '''
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
    
class Moto(Veicolo):

    def __init__(self, marca: str, modello: str, anno: int, tipo: str): #metodo costruttore che inizializza gli attributi della classe base e tipo.
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self): 
        '''
        metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, 
        nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".
        '''
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")

'''

Obiettivo
L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni 
di due specie animali usando la programmazione orientata agli oggetti in Python.

Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. 
Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche

1. Classe Specie
- Attributi:

    nome (str): Nome della specie.
    popolazione (int): Popolazione iniziale.
    tasso_crescita (float): Tasso di crescita annuo percentuale.

- Metodi:

    __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
    cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
    anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
    getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².

 

2. Sottoclassi BufaloKlingon e Elefante
Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:

    Aggiornamento della popolazione per l'anno successivo:
        Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
    Calcolo della densità di popolazione:
        Formula: popolazione / area_kmq
        Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
    Calcolo degli anni necessari per superare la popolazione di un'altra specie:
        Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra. 
        Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000. 

Example:
# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")

Result:
Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: 16
Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: 4
'''

class Specie:

    def __init__(self, popolazione: int, tasso_crescita: float): #Costruttore per inizializzare gli attributi della classe.
        self.nome = str
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self): #Metodo per aggiornare la popolazione per l'anno successivo.
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita/100))
        return self.popolazione

    def anni_per_superare(self, altra_specie: 'Specie') -> int: #Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
        anni: int = 0
        while self.popolazione <= altra_specie.popolazione:
            self.cresci()
            altra_specie.cresci()
            anni += 1
            if anni > 1000:
                return "Error"
        return anni
            
    def getDensita(self, area_kmq: float) -> int: #Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².
        anni: int = 0
        while self.popolazione / area_kmq < 1:
            self.cresci()
            anni += 1
        return anni

class BufaloKlingon(Specie):

    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__(popolazione, tasso_crescita)

class Elefante(Specie):

    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__(popolazione, tasso_crescita)

# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")