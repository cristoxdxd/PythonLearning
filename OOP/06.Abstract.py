from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def giveInformation(self):
        pass

class Mammal(Animal):
    def greet(self):
        print('Hi!')
    def giveInformation(self):
        print('I feed on milk')

class Reptile(Animal):
    def giveInformation(self):
        print('I am cold blooded')

mamifero = Mammal()
mamifero.giveInformation()

reptil = Reptile()
reptil.giveInformation()