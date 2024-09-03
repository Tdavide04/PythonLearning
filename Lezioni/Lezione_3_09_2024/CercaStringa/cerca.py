import os

def CercaParolaInNomeFile(sFile, sParola):
    sFile.find("pippo")

sRoot = input("inserisci la directory dove cercare: ")
sParola = input("inserisci la parola da cercare: ")
sOutDir = input("inserisci la directory dove mettere i file trovati: ")

bRet = False
for root, ListDir, ListFiles in os.walk(sRoot):
    print(f"Nella directory {root} ci sono {len(ListDir)} sottodirectory e {len(ListFiles)} files")
    for file in ListFiles:
        print(f"Devo cercare {sParola} in {file}")
        bRet = CercaParolaInNomeFile(file, sParola)