import inspect
class ElectronicDevice:
    power = 500
    def printit(self):
        print(f"The power is {self.power}.")

class HandOptimizableGadgets(ElectronicDevice):
    keypad = 1
    power = 250 

class SmartPhoneGadget(HandOptimizableGadgets):
    touchscreen = 1
    power = 50
    def print(self):
        print(f"The power is {self.power}.It is Touchscreen of {self.touchscreen} rating")

oneplus = SmartPhoneGadget()
oneplus.print()
telephone = ElectronicDevice()
telephone.printit()
nokia = HandOptimizableGadgets()
nokia.printit()

print(inspect.getmro(SmartPhoneGadget)) 