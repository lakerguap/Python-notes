class Dog:
    species = "Canine"
    def __init__(self, name, age):
        self.name = name #per modificare l'oggetto usiamo self.attributo
        self.age = age


dog1 = Dog("Buddy", 3) #creo un'istanza di Dog
dog2 = Dog("Charlie", 5)
print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)


#modifica di Instance varibale
dog1.name = "Max"  #si accede direttamente alla variabile
print(dog1.name)

#modifica di Class variable

Dog.species = "Feline"  #si accede direttamente alla classe
print(dog1.species)
print(dog2.species)


#single inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's name: {self.name}")

class Labrador(Dog): #Labrador eredita le caratteristiche di Dog
    def sound(self):
        print("Labrador woof")

#multilevel inheritance
class GuideDog(Labrador): #GuideDog eredita le caratteristiche di Labrador
    def guide(self):
        print(f"{self.name} guides the way")

#multiple inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly): #GoldenRetriever eredita le caratteristiche di Dog e di Friendly
    def sound(self):
        print("Golden Retriever barks!")

lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.sound()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()


#polimorfismo

