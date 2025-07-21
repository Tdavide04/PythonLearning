class Document:
    def __init__(self) -> None:
        self.text: str = ""
        
    def getText(self):
        return self.text
    
    def setText(self, new_text):
        self.text = new_text
    
    def isInText(self, word):
        if word in self.text:
            return True
        else: 
            return False
    
class Email(Document):
    def __init__(self) -> None:
        super().__init__()
        self.mittente: str = ""
        self.destinatario: str = ""
        self.title_text: str = ""
    
    def getMittente(self):
        return self.mittente
    
    def setMittente(self, mittente: str):
        self.mittente = mittente

    def getDestinatario(self):
        return self.destinatario
    
    def setDestinatario(self, destinatario: str):
        self.destinatario = destinatario

    def getTitleText(self):
        return self.title_text
    
    def setTitleText(self, title_text):
        self.title_text = title_text

    def getText(self):
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitleText()}\nMessagio: {super().getText()}"
    
    def writeToFile(self):
        file =open("/home/user/VscodeprojectDavide/PythonLearning/Esercizi/Esercizi24/document.txt", "w") 
        file.write(super().getText())
        file.close()

class File(Document):
    def __init__(self) -> None:
        super().__init__()
        self.nomePercorso = "/home/user/VscodeprojectDavide/PythonLearning/Esercizi/Esercizi24/document.txt"

    def leggiTestoDaFile(self):
        file = open("/home/user/VscodeprojectDavide/PythonLearning/Esercizi/Esercizi24/document.txt", "r")
        testo = file.read()
        file.close()
        return f"{testo}"

    def getText(self):
        return f"Percorso: {self.nomePercorso} \nContenuto: {self.leggiTestoDaFile()}"
    
if __name__ == "__main__":

    email1 = Email()
    email1.setDestinatario("Roberto")
    email1.setMittente("Giuseppe")
    email1.setTitleText("Roba")
    email1.setText("CIAOOOOOOOOOOOO 23")
    print(email1.getText())
    print(email1.isInText("23"))
    email1.writeToFile()
    

    file1 = File()
    print(file1.getText())
