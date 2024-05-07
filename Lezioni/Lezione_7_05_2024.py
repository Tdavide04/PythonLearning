class Person:
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self) -> str:
        return f"Person(name=(self.name), age=(self.age) height=(self.height), weight=(self.weight))"
    

"""da ricontrollare a casa la funzione __str__(self)"""


alice = Person("Alice W.", 45, 165, 43)
bob = Person("Bob M.", 36, 180, 75)
philip = Person("Philip", 19, 180, 76)
antonio = Person("Antonio", 20, 174, 56)
davide = Person("Davide", 20, 178, 79)
print(bob.age)

if bob.age > alice.age:
    print(bob.age)
else:
    print(alice.age)

people = [alice, bob, philip, antonio, davide]

min_age: int = float("inf")
index_min_age: int = 0
for i in range(len(people)):
    if people[i].age < min_age:
        min_age = people[i].age
        index_min_age = i

print(f"il nome della persona più giovane è {people[index_min_age].name} con età {people[index_min_age].age}")