import os

def rename_images(link_file_path, image_dir):
    # Legge i nomi dal file
    with open(link_file_path, 'r', encoding='utf-8') as file:
        pokemon_names = [line.strip() for line in file.readlines()]
    
    # Filtra i file che iniziano con "download"
    files = [f for f in os.listdir(image_dir) if f.startswith("downloads")]
    
    # Verifica la lunghezza dei nomi rispetto ai file
    if len(files) != len(pokemon_names):
        print("Il numero di file non corrisponde al numero di nomi!")
        return
    
    # Ordina i file in base al nome
    try:
        files.sort(key=lambda x: int(x.replace("downloads", "").split('.')[0]))
    except ValueError as e:
        print(f"Errore durante l'ordinamento: {e}")
        print("Controlla che tutti i file abbiano il formato corretto (es: download<number>.extension).")
        return
    
    for file, name in zip(files, pokemon_names):
        # Estrae l'indice dal nome del file
        try:
            index = int(file.replace("downloads", "").split('.')[0])  # Assicura che sia un numero
        except ValueError as e:
            print(f"Errore nel file {file}: {e}")
            continue
        
        ext = file.split('.')[-1]
        
        # Nuovo nome del file
        new_name = f"{index}_{name}.{ext}"
        
        # Percorsi completi
        old_path = os.path.join(image_dir, file)
        new_path = os.path.join(image_dir, new_name)
        
        # Rinomina il file
        os.rename(old_path, new_path)
        print(f"Rinominato: {file} -> {new_name}")

# Percorsi
link_file_path = 'test.txt'  # File contenente i nomi (uno per riga)
image_dir = 'images_pokemon'  # Directory con le immagini

# Esecuzione
rename_images(link_file_path, image_dir)
