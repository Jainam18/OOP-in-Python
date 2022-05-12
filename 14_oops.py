class Employee:
    salary = 40000
    increment = 4
    @property
    def SalaryAfterIncrement(self):
        return self.salary*self.increment
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,sai):
        self.increment = sai/self.salary
    
raju = Employee()
print(raju.salary)
print(raju.SalaryAfterIncrement)
raju.SalaryAfterIncrement = 100000
print(raju.increment)