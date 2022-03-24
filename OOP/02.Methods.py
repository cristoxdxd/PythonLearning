class Car:
    def __init__(self,license='ABC-123',color='red'):
        self.license = license,
        self.color = color
    def start(self):
        print(f'Car: license {self.license} and color {self.color}')

    @classmethod
    def speed2(cls, speed):
        print(f'Current speed: {speed}')

    @staticmethod
    def speed(speed: str):
        print(f'Current speed: {speed}')

car1 = Car()
car2 = Car(license='DEF-456', color='blue')

car1.start()
car1.speed('20 km/h')
car2.speed2('30 km/h')