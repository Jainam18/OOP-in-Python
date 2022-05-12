import inspect
class Employee:
    def __init__(self,fname,lname):
        self.lname = lname
        self.fname = fname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"
    def explain(self):
        return f"The employee is {self.fname} {self.lname} and Email is {self.email}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "First Name and Last Name are not given"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

jainam = Employee("Jainam","Rajput")
aakash = Employee("Aakash","Gupta")
print(jainam.explain())
print(aakash.explain())
# jainam.fname = "US"
# print(jainam.email)
# aakash.email = "this.that@codewithharry.com"
# # print(aakash.fname)
# del aakash.email
# print(aakash.lname)

# print(inspect.getmembers(Employee))