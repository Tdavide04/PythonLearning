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









class Student:
    def __init__(self, name: str, studyProgram: str, age: float, gender: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"Student = {self.name}, study program = {self.studyProgram}, age = {self.age}, gender = {self.gender}")
    
elena = Student("Elena", "class", 22, "female")
alessia = Student("Elena", "class", 17, "female")
erik = Student("Erik", "class", 30, "male")

elena.printInfo()




class Animal:
    def __init__(self, name: str, legs: str):
        self.name = name
        self.legs = legs
    
    def get_legs(self) -> int:
        return self.legs
    
    def set_legs(self, new_legs: int):
        self.legs = new_legs

dog = Animal("Dog", 4)
print(dog.get_legs())
dog.set_legs(3)
print(dog.get_legs())