# 1st Problem
# class Programmer:
#     def __init__(self,name,lang,salary,age):
#         self.name = name
#         self.lang = lang
#         self.salary = salary
#         self.age = age
#     def printDetails(self):
#         return f"The name of Pragrammer is {self.name}.The languages he/she know are {self.lang}.His salary is {self.salary} and age is {self.age}"

# ram = Programmer("Ram",['C','Cpp','Python','Java','R'],450000,25)
# print(ram.printDetails())


# 2nd Problem
class Calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        return self.num**2
    def cube(self):
        return self.num**3
    def squareroot(self):
        return self.num**0.5
    @staticmethod
    def greeting():
        print("Starting the Calculator")
num1 = Calculator(25)
num1.greeting()
print(num1.square())
print(num1.cube())
print(num1.squareroot())
