from abc import ABC, abstractmethod

class Volo(ABC):

    def __init__(self, codice_volo: str, numero_posti: int) -> None:
        
        self.codice_volo = codice_volo
        self.numero_posti = numero_posti
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto(self):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

class VoloCommerciale(Volo):

    def __init__(self, codice_volo: str, numero_posti: int) -> None:
        super().__init__(codice_volo, numero_posti)
        self.posti_economica = round()
        self.posti_business = 0
        self.posti_prima = 0

    def prenota_posto(self):
        return super().prenota_posto()
    def posti_disponibili(self):

        return super().posti_disponibili()