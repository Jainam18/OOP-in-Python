class Student:
    no_of_leaves = 8
    def __init__(self,name,std,div):
        self.name = name
        self.std = std
        self.div = div
    def printDetails(self):
        print(f"The name of Student is {self.name}, STD is {self.std}, Division is {self.div}")
    @classmethod
    def change_leaves(cls,changed):
        cls.no_of_leaves = changed

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

class Player:
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printPlay(self):
        print(f"Name is {self.name} and the games are {self.game}")

class CoolStudent(Player,Student):
    def printSt(self):
        print(self.div,self.game)


karan = CoolStudent("Karan",["Cricket"])
karan.printPlay()
# karan.printSt()