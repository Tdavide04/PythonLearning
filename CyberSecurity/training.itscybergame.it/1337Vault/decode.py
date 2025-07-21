import py7zr
import os
import shutil

def extract_all_7z(file_path, output_folder):
    """ Estrai il file .7z e controlla se ci sono altri .7z all'interno """
    
    os.makedirs(output_folder, exist_ok=True)
    
    # Estrai il contenuto del file .7z
    with py7zr.SevenZipFile(file_path, mode='r') as archive:
        archive.extractall(path=output_folder)

    print(f"Estratto: {file_path} in {output_folder}")
    
    # Cerca altri .7z nella cartella estratta
    for root, _, files in os.walk(output_folder):
        for file in files:
            if file.endswith(".7z"):
                new_7z_path = os.path.join(root, file)
                new_extract_folder = os.path.join(root, os.path.splitext(file)[0])
                
                # Estrai il nuovo file .7z trovato
                extract_all_7z(new_7z_path, new_extract_folder)
                
                # (Opzionale) Rimuovi il file .7z estratto per pulizia
                os.remove(new_7z_path)

# Imposta il percorso del primo file .7z
first_7z = "CyberSecurity/training.itscybergame.it/1337Vault/the_1337_vault.7z"  # Modifica con il percorso corretto
output_folder = "CyberSecurity/training.itscybergame.it/1337Vault/"  # Modifica con la cartella di destinazione

# Avvia l'estrazione ricorsiva
extract_all_7z(first_7z, output_folder)
