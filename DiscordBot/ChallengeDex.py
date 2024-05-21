import json

class Pokemon:
    def __init__(self, species, level, gender, nature, item, shiny=False, nickname=None):
        self.species = species
        self.level = level
        self.nickname = nickname if nickname else species
        self.gender = gender
        self.nature = nature
        self.item = item
        self.shiny = shiny

    def __str__(self):
        return f"{self.species} ({self.nickname}), Level: {self.level}, Gender: {self.gender}, Nature: {self.nature}, Item: {self.item}, Shiny: {self.shiny}"

class Party:
    def __init__(self) -> None:
        self.party = []

    def add_pokemon(self, pokemon):
        if len(self.party) < 6:
            self.party.append(pokemon.species)
        else:
            print("Il party è pieno! Non puoi aggiungere più di 6 Pokémon.")
            
    def remove_pokemon(self, pokemon):
        if pokemon in self.party:
            self.party.remove(pokemon)
            print(f"{pokemon.nickname} è stato rimosso dal party.")
        else:
            print(f"{pokemon.nickname} non è nel party.")

    def get_party(self):
        return self.party

class Pokedex:
    def __init__(self):
        self.entries = {}
        self.load_pokemon_data()

    def load_pokemon_data(self):
        with open('pokedex.json', 'r') as f:
            self.pokemon_data = json.load(f)

    def add_entry(self, pokemon_name):
        for pokemon in self.pokemon_data:
            if pokemon['species'] == pokemon_name:
                pokemon_id = pokemon['id']
                if pokemon_name not in self.entries:
                    self.entries[pokemon_name] = pokemon_id
                    return f"{pokemon_name} è stato aggiunto al Pokedex con ID: {pokemon_id}."
                else:
                    return f"{pokemon_name} è già nel Pokedex."
        return f"ID non trovato per {pokemon_name}."

    def remove_entry(self, pokemon_name):
        if pokemon_name in self.entries:
            del self.entries[pokemon_name]
            return f"{pokemon_name} è stato rimosso dal Pokedex."
        else:
            return f"{pokemon_name} non esiste nel Pokedex."

    def status(self):
        status_str = "Pokedex Completo:\n"
        for pokemon_name, pokemon_id in self.entries.items():
            status_str += f"{pokemon_id}: {pokemon_name}\n"
        return status_str
    
    def search_by_type(self, pokemon_type):
        found_pokemon = [pokemon['species'] for pokemon in self.pokemon_data if pokemon_type in pokemon['type']]
        if found_pokemon:
            return found_pokemon
        else:
            return f"Nessun Pokémon trovato di tipo {pokemon_type}."

    def search_by_id(self, pokemon_id):
        found_pokemon = [pokemon['species'] for pokemon in self.pokemon_data if pokemon['id'] == pokemon_id]
        if found_pokemon:
            return found_pokemon[0]
        else:
            return f"Nessun Pokémon trovato con ID {pokemon_id}."

class Challenge:
    def __init__(self) -> None:
        self.challenges = {}

    def new_challenge(self, challenge_name: str):
        challenge_name = challenge_name.title()
        if challenge_name not in self.challenges:
            self.challenges[challenge_name] = Party()
            return f"La tua challenge '{challenge_name}' è stata registrata."
        else:
            raise ValueError("Questa Challenge esiste già.")

    def remove_challenge(self, challenge_name: str):
        challenge_name = challenge_name.title()
        if challenge_name in self.challenges:
            del self.challenges[challenge_name]
            return f"La tua challenge '{challenge_name}' è stata rimossa."
        else:
            raise ValueError("Questa Challenge non esiste.")

    def add_pokemon_to_challenge(self, challenge_name: str, pokemon: Pokemon):
        challenge_name = challenge_name.title()
        if challenge_name in self.challenges:
            self.challenges[challenge_name].add_pokemon(pokemon)
        else:
            raise ValueError("Questa Challenge non esiste.")

    def get_challenge_party(self, challenge_name: str):
        challenge_name = challenge_name.title()
        if challenge_name in self.challenges:
            return self.challenges[challenge_name].get_party()
        else:
            raise ValueError("Questa Challenge non esiste.")



