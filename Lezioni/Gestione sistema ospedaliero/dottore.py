from persona import Persona

class Dottore(Persona):
    
    def __init__(self, first_name: str, last_name: str, __specialization: str, __parcel: float):
        super().__init__(first_name, last_name)
        
        if type(__specialization) != str:
            print("La specializzazione inserita non è una stringa")
            self.__specialization = None
        elif type(__parcel) != float:
            print("La parcella inserita non è un float!")
            self.__parcel = None
        else:
            self.__specialization: str = __specialization
            self.__parcel: float = __parcel
            
    def setSpecialization(self, specialization: str):
        '''
        consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stamapre un messaggio di errore, 
        ad esempio "La specializzazione inserita non è una stringa!".
        '''
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
            
    def setParcel(self, parcel: float):
        '''
        consente di impostare la parcella di un dottore, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passato al metodo un float. In caso contrario, stamapre un messaggio di errore, 
        ad esempio "La parcella inserita non è un float!".
        '''
        if type(parcel) == float:
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")
            
    def getSpecialization(self):
        #consente di ritornare la specializzazione del dottore
        return self.__specialization
    
    def getParcel(self): 
        #consente di ritornare la parcella del dottore.
        return self.__parcel
    
    def isAValidDoctor(self):
        age = self.getPersonaAge()
        first_name = self.getPersonaName()
        last_name = self.getPersonaLastName()
        '''
        stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. 
        Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. 
        In caso contrario, stampare "Doctor nome e cognome is not valid!".
        '''
        if age >= 30:
            print(f"Doctor {first_name} {last_name} is valid!")
            return True
        else:
            print(f"Doctor {first_name} {last_name} is not valid!")
            return False
            
    def doctorGreet(self):
        '''
        tale metodo richiama la funzione greet() della classe Persona. 
        Poi, stampa il seguente saluto "Sono un medico {specializzazione}"
        '''
        self.greet()
        print(f"Sono un medico {self.__specialization}")
        
        
if __name__ == "__main__":
    persona1 = Dottore("Alessandro", "Giusti", "podologo", 30.0)
    persona1.setAge(56)
    persona1.setLastName("Robbon")
    persona1.setName("Giuseppe")
    persona1.isAValidDoctor()
    persona1.doctorGreet()
    