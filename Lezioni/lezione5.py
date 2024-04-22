def add_diff_to_res(x: list[float], y: list[float], length: int) -> list[float]:
    res: list[float] = []
    for i in range(length):
        diff = x[i] - y[i]
        res.append(diff)
    return res

def subtract_lists(x: list[float], y: float) -> list[float]:
    length = min(len(x), len(y))
    res: list[float] = add_diff_to_res(x,y,length)
    return res

mylist: list[float] = [1,2,3,4,5]
y: list[float] = [2,3,4,5,6]
result: list[float] = subtract_lists(mylist, y)
print(f"Il risultato dopo la sottrazione è {result}")


s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."

def counter(s: str) -> list[float]:
    """
    Questa funzione prende una stringa in input e 
    restituisce una lista costruita nel modo seguente:
    - il primo elemento della lista contiene il numero di caratteri nella stringa
    - il secondo elemnto della lista constiene il numero di parole nella stringa
    - il terzo elemento della lista contiene il numero di parole distinte nella stringa
    - il quarto elemento della lista contiene il numero di frasi nella stringa
    """

    lista: list[int] = []
    primo = len(s)
    lista.append(primo)
    secondo = len(s.split())
    lista.append(secondo)
    parole = s.split()
    terzo = set(parole)
    lista.append(len(terzo))
    quarto = len(s.split(".")) -1
    lista.append(quarto)
    print(f"la lista è composta da {lista}")
    return lista
counter(s)

def word_count(s: str) -> dict[str, int]:
    """
    Questa funzione conta il numero di occorrenza delle parole di una stringa

    e.s.: se la stringa è "ciao come stai. tutto bene. ciao io sto bene"
    il risultato deve essere:
    {"ciao": 2, "come": 1, "stai": 1, "tutto": 1, "bene": 2, "io": 1, "sto": 1}
    """
    
    s = s.replace(".","").replace(",","").replace(";","").replace(":","").replace("!","")
    wordcount = {}
    words = s.split()

    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    filter = {}
    for key, val in wordcount.items():
        if val > 1:
            filter[key] = val
    print(f"il risultato è {filter}")
    return filter

word_count(s)

