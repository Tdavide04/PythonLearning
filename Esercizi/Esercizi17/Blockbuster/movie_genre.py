from film import Film

class Azione(Film):
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere = "Azione"
        self.__penale = 3.0

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, days):
        return self.__penale * days   
    
class Commedia(Film):
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere = "Commedia"
        self.__penale = 2.5

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, days):
        return self.__penale * days 
    
class Drama(Film):
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        self.__genere = "Drama"
        self.__penale = 2.0

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, days):
        return self.__penale * days  