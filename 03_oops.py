# SINGLE INHERITANCE
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
class Programmer(Student):
    def printProg(self):
        print(f"The name of Student is {self.name}, STD is {self.std}, Division is {self.div} and Language he knows is/are {self.language}")
shyam = Student("Shyam",6,"B")
rohan = Student("Rohan",9,"C")
karan = Programmer("Karan",14,"E")
karan.printDetails()