class Challenge:
    def __init__(self, run_type: str, version: str, TID: int, SID: int, start_date, HOF):
        self.run_type = run_type
        self.version = version
        self.TID = TID
        self.SID = SID
        self.start_date = start_date
        self.HOF = HOF
        self.info = []

    def new_challenge(self):
        pass

class Pokemon:

    def add_pokemon(self, species: str):
        self.species = species
        
        if len(party) < 6:
            party.append(self.species)
        else:
            print("Your party is full")

    def main_info(self, nickname: str, gender: str, level: int, nature: str, item: str, ability: str, shiny: bool):
        self.nickname = nickname
        self.gender = gender
        self.level = level
        self.nature = nature
        self.item = item
        self.ability = ability
        self.shiny = shiny

    def met_info(self, location: str, ball: str, met_date: str, met_level: str):
        self.location = location
        self.ball = ball
        self.met_date = met_date
        self.met_level = met_level
    

party = []

def get_party():
        print(f"Your Pokemon party contains: {party}")

#valutare togliere le classi e tutti i self



Pokemon1 = Pokemon()
Pokemon1.add_pokemon("Emboar")
get_party()