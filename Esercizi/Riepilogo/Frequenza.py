def frequency_dict(elements: list) -> dict:
    
    diz: dict = {}
    for e in elements:
        f = elements.count(e)
        diz[e] = f
    return diz

print(frequency_dict(['mela', 'banana', 'mela']))

	

