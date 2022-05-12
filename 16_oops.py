class Vector:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __add__(self,v2):
        a1 = self.a + v2.a
        b1 = self.b + v2.b
        c1 = self.c + v2.c
        return Vector(a1,b1,c1)
    def __mul__(self,v2):
        mula = self.a*v2.a
        mulb = self.b*v2.b
        mulc = self.c*v2.c
        return (mula+mulb+mulc)
    def __str__(self):
        if self.b<0:
            return f"{self.a}i - {-self.b}j + {self.c}k"
        elif self.c<0:
            return f"{self.a}i + {self.b}j - {-self.c}k"
        return f"{self.a}i + {self.b}j + {self.c}k"
    
v1 = Vector(5,4,7)
v2 = Vector(3,6,9)
print(v1)
print(v2)
print(v1 + v2)
print(v1*v2)