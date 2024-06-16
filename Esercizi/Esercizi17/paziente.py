from persona import Persona

class Paziente(Persona):
    
    def __init__(self, first_name: str, last_name: str, __idCode: str):
        super().__init__(first_name, last_name)
        
        if type(__idCode) != str:
            print("idCode del paziente non è una stringa")
        else:
            self.__idCode = __idCode
    
    def setPazientIdCode(self, idCode: str): 
        #consente di impostare il codice identificativo del paziente.
        
        if type(idCode) != str:
            print("idCode del paziente non è una stringa")
        else:
            self.__idCode = idCode
            
    def getPazientidCode(self): 
        #consente di ritornare il codice identificativo del paziente.
        return self.__idCode
    
    def getPazienteName(self):
        return self.getPersonaName()
    
    def getPazientLastName(self):
        return self.getPersonaLastName()
    
    def patientInfo(self): 
        #stampa in output le informazioni del paziente in questo modo:
        #  "Paziente: {nome} {cognome}
        # ID: {codice identificativo}"
        first_name = self.getPersonaName()
        last_name = self.getPersonaLastName()
        
        print(f"Paziente: {first_name} {last_name}")
        print(f"ID: {self.__idCode}")
        

if __name__ == "__main__":
    persona1 = Paziente("Alessandro", "Giusti", "C982AR")
    persona1.setAge(56)
    persona1.setLastName("Robbon")
    persona1.setName("Giuseppe")
    persona1.getPazientidCode()
    persona1.patientInfo()