def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    
    for key, value in dizionario.items():
        if value == valore:
            return key
    else:
        return None