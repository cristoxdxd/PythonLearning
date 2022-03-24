class Position:
    def __init__(self, positions: tuple) -> None:
        self.x, self.y = positions
    def setX(self,Xvalue):
        self.x = Xvalue
    def setY(self,Yvalue):
        self.y = Yvalue
    def getCoordinates(self):
        return self.x, self.y