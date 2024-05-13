class Zoo:
    def __init__(self, fences = [], zoo_keepers = []) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def add_fences(self, fence):
        self.fences.append(fence)


    def get_fences(self) -> list:
        return self.fences
    


class Animal:

    def __init__(self, name: str, age: int) -> None:
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name:str):
        self.name = name

    def set_age(self, age:int):
        self.age = age

    def __str__(self) -> str:
        return f"Animal(name = {self.name}, age = {self.age}"
    
class Person(Animal):

    def talk(self) -> str:
        return f"Ciao, mi chiamo {self.name}"
    
    def __str__(self) -> str:
        return f"Person(name = {self.name}, age = {self.age})"
    
class Student(Person):

    def __init__(self, name: str, age: str, id: int):
        super().__init__(name, age)
        self.id = id

    def talk(self) -> str:
        s = super().talk()
        return f"Ciao sono uno studente e mi chiamo {self.name}"
    
a = Student(name = "ufvbeug", age = 28, id = 1836)
print(a.talk())
