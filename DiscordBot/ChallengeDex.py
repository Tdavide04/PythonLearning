import discord
from discord.ext import commands
import json

# Load your bot token from a config file or environment variable
BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Pokemon class
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

# Pokedex class
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

# Challenge class
class Challenge:
    class Party:
        def __init__(self):
            self.party = []

        def add_pokemon(self, pokemon):
            if len(self.party) < 6:
                self.party.append(pokemon.species)
                return f"{pokemon.nickname} è stato aggiunto al party."
            else:
                return "Il party è pieno! Non puoi aggiungere più di 6 Pokémon."

        def remove_pokemon(self, pokemon):
            if pokemon.species in self.party:
                self.party.remove(pokemon.species)
                return f"{pokemon.nickname} è stato rimosso dal party."
            else:
                return f"{pokemon.nickname} non è nel party."

        def get_party(self):
            return self.party

    def __init__(self) -> None:
        self.challenges = {}

    def new_challenge(self, challenge_name: str):
        challenge_name = challenge_name.title()
        if challenge_name not in self.challenges:
            self.challenges[challenge_name] = Party()
            return f"La tua challenge '{challenge_name}' è stata registrata."
        else:
            return "Questa Challenge esiste già."

    def remove_challenge(self, challenge_name: str):
        challenge_name = challenge_name.title()
        if challenge_name in self.challenges:
            del self.challenges[challenge_name]
            return f"La tua challenge '{challenge_name}' è stata rimossa."
        else:
            return "Questa Challenge non esiste."

    def add_pokemon_to_challenge(self, challenge_name: str, pokemon: Pokemon):
        challenge_name = challenge_name.title()
        if challenge_name in self.challenges:
            return self.challenges[challenge_name].add_pokemon(pokemon)
        else:
            return "Questa Challenge non esiste."

    def get_challenge_party(self, challenge_name: str):
        challenge_name = challenge_name.title()
        if challenge_name in self.challenges:
            return self.challenges[challenge_name].get_party()
        else:
            return "Questa Challenge non esiste."

# Global instances
pokedex = Pokedex()
challenge_manager = Challenge()

# Bot commands
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def add_challenge(ctx, challenge_name: str):
    response = challenge_manager.new_challenge(challenge_name)
    await ctx.send(response)

@bot.command()
async def remove_challenge(ctx, challenge_name: str):
    response = challenge_manager.remove_challenge(challenge_name)
    await ctx.send(response)

@bot.command()
async def add_pokemon(ctx, challenge_name: str, species: str, level: int, gender: str, nature: str, item: str, shiny: bool = False, nickname: str = None):
    pokemon = Pokemon(species, level, gender, nature, item, shiny, nickname)
    response = challenge_manager.add_pokemon_to_challenge(challenge_name, pokemon)
    await ctx.send(response)

@bot.command()
async def show_party(ctx, challenge_name: str):
    response = challenge_manager.get_challenge_party(challenge_name)
    await ctx.send(f"Party per la challenge '{challenge_name}': {', '.join(response)}")

@bot.command()
async def add_pokedex_entry(ctx, pokemon_name: str):
    response = pokedex.add_entry(pokemon_name)
    await ctx.send(response)

@bot.command()
async def remove_pokedex_entry(ctx, pokemon_name: str):
    response = pokedex.remove_entry(pokemon_name)
    await ctx.send(response)

@bot.command()
async def pokedex_status(ctx):
    response = pokedex.status()
    await ctx.send(f"Pokedex:\n{response}")

@bot.command()
async def search_by_type(ctx, pokemon_type: str):
    response = pokedex.search_by_type(pokemon_type)
    await ctx.send(f"Pokémon di tipo {pokemon_type}: {', '.join(response)}")

@bot.command()
async def search_by_id(ctx, pokemon_id: int):
    response = pokedex.search_by_id(pokemon_id)
    await ctx.send(response)

bot.run(BOT_TOKEN)
