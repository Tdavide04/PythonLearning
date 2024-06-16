class Persona:

    def __init__(self, first_name: str, last_name: str):
        if type(first_name) != str:
            print("Il nome di battesimo non è una stringa!")
            self.__first_name = None
        elif type(last_name) != str:
            print("Il cognome non è una stringa!")
            self.__last_name = None
        else:
            self.__first_name = first_name
            self.__last_name = last_name
            self.__age = 0

    def __str__(self):
        return f"Nome: {self.__first_name}, Cognome: {self.__last_name}, Età: {self.__age}"
    
    def setName(self, first_name: str):
        '''
        consente di impostare il nome di una persona, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passata al metodo una stringa. 
        In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
        '''
        if type(first_name) == str:
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")
            
    def getPersonaName(self):
        return self.__first_name

    def setLastName(self, last_name: str):
        '''
        consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passata al metodo una stringa. 
        In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!"
        '''
        if type(last_name) == str:
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")
            
    def getPersonaLastName(self):
        return self.__last_name

    def setAge(self, age: int):
        '''
        consente di impostare l'età di una persona, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passato al metodo un numero intero. 
        In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
        '''
        if type(age) == int:
            self.__age = age
        else:
            print("L'età deve essere un numero intero!")
            
    def getPersonaAge(self):
        return self.__age
            
    def greet(self):
        #stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")



if __name__ == "__main__":
    persona1 = Persona("Alessandro", "Giusti")
    persona1.setAge(56)
    persona1.setLastName("Robbon")
    persona1.setName("Giuseppe")
    persona1.greet()