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
            pokemon_names[f"downloads{i:04d}"] = name
        except IndexError:
            print(f"Errore durante l'analisi del link: {link}")
    
    # Dizionario per tracciare i nomi già usati
    used_names = {}

    # Rinomina i file
    for filename in os.listdir(image_dir):
        if filename.startswith("downloads"):
            base_name = filename.split('.')[0]
            ext = filename.split('.')[-1]
            if base_name in pokemon_names:
                original_name = pokemon_names[base_name]
                new_name = original_name

                # Gestisce le collisioni aggiungendo un suffisso univoco
                while new_name in used_names:
                    count = used_names[new_name]
                    new_name = f"{original_name}_{count}"
                    used_names[original_name] += 1
                
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
                print(f"Nome non trovato per: {filename}")

# Percorsi
link_file_path = 'URLs/URLs.txt'  # Sostituire con il percorso reale del file
image_dir = 'images_pokemon/'  # Sostituire con il percorso della cartella immagini

# Esecuzione
rename_images(link_file_path, image_dir)
