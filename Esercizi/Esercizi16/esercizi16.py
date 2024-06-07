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
    
    def __init__(self) -> None:
        self.title = str
        self.review = list[int]
        self.rate = sum(self.review)/len(self.review)

    def set_title(self, title: str): # Imposta il titolo del media.
        self.title = title

    def get_title(self): # Restituisce il titolo del media.
        return self.title
    
    def aggiungiValutazione(self, voto: int): # Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
        if voto <= 5:
            self.review.append(voto)
        else:
            raise ValueError("Error value for a review. It have to be 5 or inferior")
        
    def getMedia(self) -> float: #Calcola e restituisce la media delle valutazioni.
        return self.rate
    
    def getRate(self): 
        '''Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1, 
        "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, 
        "Grandioso" se il voto medio si avvicina a 5.
        '''

        if round(self.rate) == 1:
            return "Terribile"
        if round(self.rate) == 2:
            return "Brutto"
        if round(self.rate) == 3:
            return "Normale"
        if round(self.rate) == 4:
            return "Bello"
        if round(self.rate) == 5:
            return "Grandioso"

    def ratePercentage(self, voto): #Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
        for e in self.review:
            pass

    def recensione(self):
        




class Film(Media):
    pass