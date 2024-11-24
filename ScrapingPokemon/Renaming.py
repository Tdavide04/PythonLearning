import os

# Lista dei Pokémon del Pokédex Nazionale (fino a 1120)
pokemon_names = [
    "Bulbasaur", "Ivysaur", "Venusaur", 
    "Charmander", "Charmeleon", "Charizard", 
    "Squirtle", "Wartortle", "Blastoise", 
    "Caterpie", "Metapod", "Butterfree", 
    "Weedle", "Kakuna", "Beedrill", 
    "Pidgey", "Pidgeotto", "Pidgeot", 
    "Rattata", "Raticate", "Spearow", 
    "Fearow", "Ekans", "Arbok", 
    "Pikachu", "Raichu", "Sandshrew", 
    "Sandslash", "Nidoran♀", "Nidorina", 
    "Nidoqueen", "Nidoran♂", "Nidorino", 
    "Nidoking", "Clefairy", "Clefable", 
    "Vulpix", "Ninetales", "Jigglypuff", 
    "Wigglytuff", "Zubat", "Golbat", 
    "Oddish", "Gloom", "Vileplume", 
    "Paras", "Parasect", "Venonat", 
    "Venomoth", "Diglett", "Dugtrio", 
    "Meowth", "Persian", "Psyduck", 
    "Golduck", "Machop", "Machoke", 
    "Machamp", "Bellsprout", "Weepinbell", 
    "Victreebel", "Tentacool", "Tentacruel", 
    "Geodude", "Graveler", "Golem", 
    "Ponyta", "Rapidash", "Magnemite", 
    "Magneton", "Farfetch'd", "Doduo", 
    "Dodrio", "Seel", "Dewgong", 
    "Grimer", "Muk", "Shellder", 
    "Cloyster", "Gastly", "Haunter", 
    "Gengar", "Onix", "Steelix", 
    "Drowzee", "Hypno", "Krabby", 
    "Kingler", "Exeggcute", "Exeggutor", 
    "Cubone", "Marowak", "Hitmonlee", 
    "Hitmonchan", "Lickitung", "Lickilicky", 
    "Koffing", "Weezing", "Rhyhorn", 
    "Rhydon", "Chansey", "Blissey", 
    "Tangela", "Tangrowth", "Kangaskhan", 
    "Horsea", "Seadra", "Goldeen", 
    "Seaking", "Staryu", "Starmie", 
    "Mr. Mime", "Scyther", "Jynx", 
    "Electabuzz", "Magmar", "Pinsir", 
    "Tauros", "Magikarp", "Gyarados", 
    "Lapras", "Ditto", "Eevee", 
    "Vaporeon", "Jolteon", "Flareon", 
    "Porygon", "Porygon2", "Omanyte", 
    "Omastar", "Kabuto", "Kabutops", 
    "Aerodactyl", "Snorlax", "Articuno", 
    "Zapdos", "Moltres", "Mewtwo", 
    "Mew", "Chikorita", "Bayleef", "Meganium", 
    "Cyndaquil", "Quilava", "Typhlosion", 
    "Totodile", "Croconaw", "Feraligatr", 
    "Sentret", "Furret", "Hoothoot", 
    "Noctowl", "Ledyba", "Ledian", 
    "Spinarak", "Ariados", "Chinchou", 
    "Lanturn", "Pichu", "Cleffa", 
    "Igglybuff", "Togepi", "Togetic", 
    "Natu", "Xatu", "Mareep", 
    "Flaaffy", "Ampharos", "Bellossom", 
    "Sunkern", "Sunflora", "Politoed", 
    "Hoppip", "Skiploom", "Jumpluff", 
    "Aipom", "Yanma", "Quagsire", 
    "Espeon", "Umbreon", "Murkrow", 
    "Slowking", "Miltank", "Blissey", 
    "Registeel", "Regice", "Regirock", 
    "Lugia", "Ho-Oh", "Celebi"
]

# Percorso della cartella con i file da rinominare
folder_path = "images_pokemon"

# Itera sui file e rinomina utilizzando i nomi dei Pokémon
for i, pokemon_name in enumerate(pokemon_names, start=1):
    old_file_name = os.path.join(folder_path, f"download{i:04d}.png")
    new_file_name = os.path.join(folder_path, f"{i:04d}_{pokemon_name}.png")
    
    if os.path.exists(old_file_name):  # Verifica che il file esista
        os.rename(old_file_name, new_file_name)
        print(f"Rinominato: {old_file_name} -> {new_file_name}")
    else:
        print(f"File non trovato: {old_file_name}")
