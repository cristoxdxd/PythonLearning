class Character:

    # Attribute
    def __init__(self, name, type, age):
        self.CharacterName = name
        self.type = type        
        self.age = age

    # Getters & Setters
    def getCharacterName(self):
        return self.CharacterName

    def setCharacterName(self, newName: str):
        self.CharacterName = newName

    # Methods
    def Greet(self):
        print(f'Hi, I\'m a character\nMy name is {self.CharacterName} and I\'m a {self.type}')
    

personaje1 = Character('Batman','Hero',35)
personaje2 = Character('Spiderman','Hero',23)

personaje1.Greet()
personaje2.Greet()

print(personaje2.getCharacterName())
personaje2.setCharacterName('Venom')
print(personaje2.getCharacterName())
