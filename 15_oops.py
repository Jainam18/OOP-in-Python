class ComplexNum:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return ComplexNum(self.a+other.a,self.b+other.b)
    def __mul__(self,other):
        mulReal =  self.a*other.a - self.b*other.b
        mulImg =  self.a*other.b + self.b*other.a
        return ComplexNum(mulReal, mulImg)
    def __str__(self):
        if self.b<0:
            return f"{self.a} - {-self.b}i"
        return f"{self.a} + {self.b}i"

c1 = ComplexNum(5,4)
c2 = ComplexNum(5,-4)
print(c1)
print(c2)
print(c1+c2)
print(c1*c2)
