import os

def CercaParolaInNomeFile(sFile, sParola) -> bool:
    sFileLower = sFile.lower()
    sParolaLower = sParola.lower()
    if sFile.find(sParolaLower) >= 0:
        return True
    return False

sRoot = input("Inserisci la directory dove cercare: ")
sParola = input("Inserisci la parola da cercare: ")
sOutDir = input("Inserisci la directory dove mettere i file trovati: ")

bRet = False
for root, ListDir, ListFiles in os.walk(sRoot):
    print(f"Nella directory {root} ci sono {len(ListDir)} sottodirectory e {len(ListFiles)} files")
    for file in ListFiles:
        print(f"Devo cercare {sParola} in {file}")
        bRet = CercaParolaInNomeFile(file, sParola) 
        if bRet:
            print(f"Trovata parola in file {file}")
        else:
            sFilePathCompleto = os.path.join(root, file)
            bRet = CercaParolaInContenutoFile(sFilePathCompleto, sParola)