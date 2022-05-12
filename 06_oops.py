class Employee:
    var1 = 34
    def __init__(self):
        self.var1 = 64
        self.classvar = 42
    
class Prog(Employee):
    var1 = 99
    def __init__(self):
        super().__init__()
        self.var1 = 11
        self.classvar = 101
        self.var2 = 455

a = Employee()
b = Prog()
print(a.var1)
print(a.classvar)
print(b.var1)
print(b.classvar)
print(b.var2)
