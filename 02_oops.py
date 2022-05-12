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

shyam = Student("Shyam",6,"B")
rohan = Student("Rohan",9,"C")
yash = Student("Yash",4,"A")
karan = Student.from_dash("Karan-7-A")
# print(rohan.no_of_leaves)
# rohan.change_leaves(34)
# print(yash.no_of_leaves)
karan.printDetails()