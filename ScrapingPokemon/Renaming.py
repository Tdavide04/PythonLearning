import os

def rename_images(link_file_path, image_dir):
    # Legge il file contenente i link
    with open(link_file_path, 'r') as file:
        links = file.readlines()
    
    # Crea un dizionario con l'indice del file e il nome del Pokémon
    pokemon_names = {}
    for i, link in enumerate(links, start=1):
        try:
            name = link.strip().split('/')[-1].split('.')[0][4:]  # Rimuove "####"
            pokemon_names[i] = name  # Usa l'indice come chiave
        except IndexError:
            print(f"Errore durante l'analisi del link: {link}")
    
    # Dizionario per tracciare i nomi già usati
    used_names = {}

    # Rinomina i file
    for filename in os.listdir(image_dir):
        if filename.startswith("downloads"):
            print(f"File trovato: {filename}")  # Aggiungi una stampa per diagnosticare
            base_name = filename.split('.')[0]  # Ad esempio "downloads0001"
            ext = filename.split('.')[-1]
            
            # Estrai l'indice (numerico) dal nome del file "downloads0001"
            try:
                # Rimuovi il prefisso "downloads" per ottenere solo il numero
                index_pokedex = int(base_name[9:])  # Ad esempio "0001" diventa 1
                if index_pokedex in pokemon_names:
                    pokemon_name = pokemon_names[index_pokedex]
                    new_name = f"{index_pokedex}_{pokemon_name}"

                    # Gestisce le collisioni aggiungendo un suffisso univoco
                    while new_name in used_names:
                        count = used_names[new_name]
                        new_name = f"{index_pokedex}_{pokemon_name}_{count}"
                        used_names[new_name] += 1
                    
                    # Aggiorna il dizionario per i nomi usati
                    if new_name not in used_names:
                        used_names[new_name] = 1
                    else:
                        used_names[new_name] += 1

                    # Rinomina il file
                    old_path = os.path.join(image_dir, filename)
                    new_path = os.path.join(image_dir, f"{new_name}.{ext}")
                    os.rename(old_path, new_path)
                    print(f"Rinominato: {filename} -> {new_name}.{ext}")
                else:
                    print(f"Nome non trovato per l'indice {index_pokedex} nel file: {filename}")
            except ValueError as e:
                print(f"Errore nel parsing dell'indice in: {filename}, errore: {e}")

# Percorsi
link_file_path = 'URLs/URLs.txt'  # Sostituire con il percorso reale del file
image_dir = 'images_pokemon'  # Sostituire con il percorso della cartella immagini

# Esecuzione
rename_images(link_file_path, image_dir)
