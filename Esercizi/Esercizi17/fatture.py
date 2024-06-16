from paziente import Paziente
from dottore import Dottore

class Fattura:
    
    def __init__(self, patients: list[Paziente], doctor: Dottore) -> None:
        
        self.doctor = doctor
        
        if self.doctor.isAValidDoctor():
            self.patients = {}
            for patient in patients:
                self.patients[patient.getPazientidCode()] = patient.getPersonaLastName()
            self.fatture: int = len(self.patients)
            self.salary: int = 0
        else:
            self.patient = None
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    
    def getSalary(self):
        #deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.
        self.salary = len(self.patients) * self.doctor.getParcel()
        return self.salary
    
    def getFatture(self): 
        #deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.
        
        self.fatture = len(self.patients)
        return self.fatture
    
    def addPatient(self, newPatient: Paziente):
        '''
        consente di aggiungere un paziente alla lista di pazienti di un dottore, 
        aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  
        Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
        '''
        self.patients[newPatient.getPazientidCode()] = newPatient.getPersonaLastName()
        self.getSalary()
        self.getFatture()
        print(f"Alla lista del Dottor cognome è stato aggiunto il paziente {newPatient}")
        
    def removePatient(self, idCode: str):
        '''
        consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, 
        aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). 
        Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
        '''
        if idCode in self.patients:
            del self.patients[idCode]
            self.getSalary()
            self.getFatture()
            print(f"Alla lista del Dottor {self.doctor.getPersonaLastName()} è stato rimosso il paziente {idCode}")
        else:
            print(f"Il paziente con codice identificativo {idCode} non è stato trovato.")
    
    def patientsList(self):
        return self.patients
        
        
if __name__ == "__main__":
    dottore1 = Dottore("Alessandro", "Giusti", "podologo", 30.0)
    dottore1.setAge(56)
    dottore1.setLastName("Robbon")
    dottore1.setName("Giuseppe")
    paziente1 = Paziente("Roberto", "Sgarbi", "C982AR")
    paziente1.setAge(30)
    paziente2 = Paziente("Luca", "Giustiniani", "C982A3")
    paziente2.setAge(29)
    patients_list = [paziente1, paziente2]
    fattura1 = Fattura(patients_list, dottore1)
    paziente3 = Paziente("Marco", "Bianchi", "C982A4")
    paziente3.setAge(16)
    fattura1.addPatient(paziente3)
    fattura1.removePatient("C982AR")
    print(fattura1.patientsList())
    