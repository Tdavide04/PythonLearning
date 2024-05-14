'''
Creaiamo un sistema di gestione di uno zoo virtuale

Sistema di gestione dello zoo virtuale

Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. 
Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. 
I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un nome, un cognome, e un id. 
Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, 
ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, 
l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, 
habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), 
Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:

ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

Fences:

Fence(area=100, temperature=25, habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)

#########################
Fra un recinto e l'altro mettete 30 volte il carattere #.
'''


class Zoo:
    def __init__(self, fences, zoo_keepers) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self):
        print("Guardians:")
        for keeper in self.zoo_keepers:
            print(f"Zookeeper(name = {keeper.name}, surname = {keeper.surname}, id = {keeper.id})")
            
        print("Fences:")
        for fence in self.fences:
            print(f"Fence(area = {fence.area}, temperature = {fence.temperature}, habitat = {fence.habitat})")
            print("with animal:")
            for animal in fence.animals:
                print(f"Animal(name = {animal.name}, species = {animal.species}, age = {animal.age})")
            print("#"*30)


class Animal:
 
    def __init__(self, name, species, age, height, width, preferred_habitat) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
    

class Fence:
    def __init__(self, area, temperature, habitat) -> None:
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.list_of_animal = []
        
class ZooKeepers:
    def __init__(self, name, surname, id) -> None:
        self.name = name
        self.surname = surname
        self.id = id

    def get_name(self):
        return self.name
    
    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat == fence.habitat:
            fence.list_of_animal.append(animal.name)

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in Fence.list_of_animal:
            animal.pop(Fence.list_of_animal)

    def feed(self, animal: Animal):
        pass
    
    def clean(self, fence: Fence):
        pass
    



Matteo = ZooKeepers("matteo", "blabla", 1763)
Gatto = Animal("Gatto", "gattus", 98, 120, 80, "Continental")
Continental = Fence(100, 38, "Continental")
Matteo.add_animal(Gatto, Continental)
print(Continental.list_of_animal)
