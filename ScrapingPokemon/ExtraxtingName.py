import re

# Funzione per estrarre il nome del Pokémon dal link
def estrai_nome(link):
    # Usa una regex per estrarre il nome del Pokémon tra l'ID (es. 0001) e l'estensione .png
    match = re.search(r'/([0-9]+)([a-zA-Z_]+)\.png', link)
    if match:
        return match.group(2)  # Restituisce solo il nome del Pokémon (la seconda parte)
    return None  # Se non si trova il nome, restituisce None

# Funzione per leggere i link da un file e scrivere i nomi in un altro
def analizza_link(input_file, output_file):
    with open(input_file, 'r') as f:
        links = f.readlines()  # Legge tutti i link dal file di input

    nomi_pokemon = []

    for link in links:
        link = link.strip()  # Rimuove eventuali spazi bianchi all'inizio e alla fine
        if link:  # Verifica che il link non sia vuoto
            nome = estrai_nome(link)
            if nome:
                nomi_pokemon.append(nome)  # Aggiungi il nome estratto alla lista

    # Scrivi i nomi dei Pokémon nel file di output
    with open(output_file, 'w') as f:
        for nome in nomi_pokemon:
            f.write(nome + '\n')  # Scrive ogni nome su una nuova riga
# Esegui l'analisi
input_file = 'URLs/URLs.txt'  # Il file di input contenente i link
output_file = 'test.txt'  # Il file di output dove verranno scritti i nomi

analizza_link(input_file, output_file)

print("Nomi dei Pokémon estratti e scritti nel file:", output_file)
