'''
### CLASSE: Film
In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:
init(id, title): metodo costruttore.
setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
getID(): che consente di ritornare il valore del codice identificativo di un film.
getTitle(): che consente di ritornare il valore del titolo di un film.
isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
 
### CLASSI GENERE
Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, che equivale al genere di film (genere="Azione", nella classe Azione) ed un attributo privato di tipo float chiamato penale. I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, i film drammatici hanno una penale di 2 euro al giorno.

- Per ognuna di queste classi si implementi un metodo chiamato:
getGenere(), che ritorna il genere di film
getPenale(), che ritorna il valore della penale
calcolaPenaleRitardo(), che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.
Le tre classi Azione, Commedia e Drama devono essere contenute nel file "movie_genre.py".
 
### CLASSE: Noleggio
In un file "noleggio.py", creare una classe Noleggio.
Questa classe deve avere come attributi una lista di film contenuti in negozio (film_list), un dizionario (rented_film) che ha come chiave un numero intero rappresentante l'id del cliente che ha affittato il film e per valore una lista contenente i film affittati dal cliente.
 
- Definire i seguenti metodi:
init(film_list): tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.
isAvaible(film): tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false in caso contrario. Se il film è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!". Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!".
rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto, il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile, rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
la chiave sarà l'id del cliente che noleggia (id_client)
il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere aggiunto alla lista dei film noleggiati dal cliente dato.  Se il cliente ha potuto noleggiare il film richiesto, stampare: "Il cliente {clientId} ha noleggiato {titolo_film}!". Se, invece, il film richiesto non è disponibile pe il noleggio, stampare: Non è possibile nolegiare il film {titolo_film}!".
giveBack(film, clientID, days): questo metodo consente di restituire un film noleggiato in negozio, ed ha come argomenti il film da restituire, il codice ID del client che restituisce il film, il numero dei giorni in cui il cliente ha tenuto il film per se.  Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, deve essere riaggiunto alla lista dei film disponibili in negozio (film_list). Successivamente, il metodo deve calcolare la penale che il cliente deve pagare utilizzando l'opposito metodo. Stampare la penale che il cliente deve pagare: "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".
printMovies(): stampa la lista di tutti i film disponibili in negozio. Ogni film deve essere stampato in questo modo: "{titolo_film} - {genere_film} -"
printRentMovies(clientID): questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.
### Creazione di Test Case con UnitTest
Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Film, Azione, Commedia, Dramma, e Noleggio. 

Istruzioni
Creare un nuovo file Python denominato "test_blockbuster.py".
Importare il modulo unittest e tutte le classi definite.
Creare una sola classe di test chiamata TestFilm che eredita da unittest.TestCase.
 
Configurazione Iniziale:
- Utilizzare il metodo setUp per creare l'ambiente di test:
   - In setUp, istanziare 10 film (5 di azione, 4 commedie e 1 drammatico) e aggiungerli a una lista di film.
   - Creare un oggetto Noleggio utilizzando la lista di film creata.

Testare la Disponibilità di un Film (isAvaible):
- Scrivere un test per verificare che un film disponibile ritorni True.
- Scrivere un test per verificare che un film non disponibile ritorni False.

Testare il Noleggio di un Film (rentAMovie):
- Scrivere un test per verificare che un film disponibile possa essere noleggiato correttamente.
- Dopo il noleggio, verificare che il film non sia più disponibile.
- Verificare che il film noleggiato appaia nella lista dei film noleggiati dal cliente.

Testare il Noleggio di un Film Non Disponibile:
- Noleggiare un film con un cliente.
- Provare a noleggiare lo stesso film con un altro cliente e verificare che non sia possibile.

Testare la Restituzione di un Film (giveBack):
- Noleggiare un film e poi restituirlo.
- Verificare che il film restituito sia nuovamente disponibile.
- Verificare che il film restituito non sia più nella lista dei film noleggiati dal cliente.

Testare il Calcolo della Penale di Ritardo (calcolaPenaleRitardo):
- Scrivere test per verificare il calcolo della penale di ritardo per film di diversi generi (azione, commedia, dramma).

Testare la Stampa dei Film Disponibili (printMovies):
- Verificare che la lista dei film disponibili contenga i titoli corretti.

Testare la Stampa dei Film Noleggiati da un Cliente (printRentMovies):
- Noleggiare uno o più film per un cliente.
- Verificare che la stampa dei film noleggiati contenga i titoli corretti.
'''