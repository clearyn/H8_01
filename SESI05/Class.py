##Python Class
print("\n\n> Define a class with python")
class Dog:
    # Classs attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Pass argument to class parameter
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
print("Class name:", buddy.name,"with age: ", buddy.age, ", species:", buddy.species)


##Instance method
print("\n\n> Instance method inside method")

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")
#Test instance
print(jim.description())
print(jim.speak("Woof woof"))


##Parent vs Child Classes
print("\n\n> Parent vs Child Classes")
class Mother:
    def __init__(self, nama, warna_rambut = 'black'):
        self.warna_rambut = warna_rambut
        self.nama = nama

    def getWarnaRambut(self):
        return self.warna_rambut
class Child(Mother):
    def __init__(self,nama, warna_rambut):
        super().__init__(nama, warna_rambut)

m = Mother('ani')
print(m.nama, m.warna_rambut)
c = Child('risa', 'green')
print(m.nama, c.warna_rambut)

print("\n\n> Parent vs Child Classes")
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    def speak(self, sound="Awoo"):
        return f"{self.name} says {sound}"

class Bulldog(Dog):
    def speak(self, sound="Warg"):
        return f"{self.name} says {sound}"

buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
miles = JackRussellTerrier("Miles", 4)
print(buddy.speak())
print(jack.speak())
print(miles.speak())
print(isinstance(miles, Dog))