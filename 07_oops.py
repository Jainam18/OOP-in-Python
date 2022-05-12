# DIAMOND SHAPE PROBLEM\
import inspect
class A:
    def met(self):
        print("This is from class A")

class B(A):
    # def met(self):
    #     print("This is from class B")
    pass

class C(A):
    # def met(self):
    #     print("This is from class C")
    pass

class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()
d.met()

print(inspect.getmro(D)) 