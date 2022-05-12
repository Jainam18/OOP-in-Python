from os import stat_result


class Animals:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
class Pets(Animals):
    def __init__(self, name, age,vaccine):
        super().__init__(name, age)
        self.vaccine = vaccine
class Dogs(Pets):
    def __init__(self, name, age, vaccine):
        super().__init__(name, age, vaccine)
    @staticmethod
    def bark():
        print("Dog Barks")

d = Dogs("Max",3,"Yes")
d.bark()