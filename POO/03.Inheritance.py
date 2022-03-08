class Pet:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    
    
    def makeNoise(self):
        print(f'Generic {self.name} noise')
    
class Dog(Pet):
    def __init__(self, name, gender, race):
        super().__init__(name, gender)
        self.race = race
    
    def makeNoise(self):
        print('Bark')

    def playDead(self):
        print(f'*{self.name} plays dead*')

class Cat(Pet):
    def __init__(self, name, gender,color):
        super().__init__(name, gender)
        self.color = color

    def makeNoise(self):
        print('Meow')

    def followLight(self):
        print(f'*{self.name} plays with the laser*')

unknowedPet = Pet('Paxy','Female')
myDog = Dog("Jack", "Male", "Pitbull")
myCat = Cat('Babura','Female','brown')

unknowedPet.makeNoise()
myDog.makeNoise()
myCat.makeNoise()
myDog.playDead()
myCat.followLight()
