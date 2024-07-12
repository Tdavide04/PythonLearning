from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(testoInChairo):
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(testoCodifica):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        self.chiave = chiave
    
    def codifica(self, testoInChairo):
        testoInChairo = testoInChairo.lower()
        testoInChairo = str(list(testoInChairo))
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        testo_codificato = []

        while self.chiave > 26:
            self.chiave -= 26

        for i in testoInChairo:
            for j in alfabeto:
                if i == j:
                    indice = alfabeto.index(j) + self.chiave
                    if indice <= len(alfabeto):
                        j = alfabeto[indice]
                        testo_codificato.append(j)
                    else:
                        indice = indice - len(alfabeto)
                        j = alfabeto[indice]
                        testo_codificato.append(j)    
        testo_codificato = "".join(testo_codificato)
        return testo_codificato

    def decodifica(self, testoCodifica):
        return super().decodifica()
    

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n) -> None:
        self.n = n

    def codifica(testoInChairo):
        pass


if __name__ == "__main__":

    doc = CifratoreAScorrimento(48303287)
    print(doc.codifica("Ciaozzz"))