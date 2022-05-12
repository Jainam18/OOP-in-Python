class C_2D:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C_3D(C_2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

a = C_2D(4,8)
b = C_3D(7,15,8)

print(a)
print(b)