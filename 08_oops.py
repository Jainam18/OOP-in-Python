from abc import ABC,abstractmethod 
class Base(ABC):
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(Base):
    type = "Rectangle"
    side = 4
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def printArea(self):
        return self.length*self.breadth

class Square(Base):
    type = "Square"
    side = 4
    def __init__(self,length):
        self.length = length
    def printArea(self):
        return self.length**2

rec1 = Rectangle(15,4)
sq1 = Square(10)
