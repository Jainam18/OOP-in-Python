class Train:
    def __init__(self,tname,tfare,tseats):
        self.tname = tname
        self.tfare = tfare
        self.tseats = tseats
    def bookTicket(self):
        print(f"There are right now {self.tseats} number of seats")
        if(self.tseats<=1):
            print("So Cant Book Ticket.Train is Full")
        else:
            self.tseats = self.tseats - 1
            print(f"Ticket is Booked for fare of {self.tfare} Rs")
    def checkSeats(self):
        return f"The number of seats left in Train are {self.tseats}"
    def getFare(self):
        return f"The Fare of {self.tname} is {self.tfare} Rs"
    def getInfo(self):
        return f"The name of the train is {self.tname}.The number of seats left in Train are {self.tseats}.The Fare of {self.tname} is {self.tfare} Rs "
garibrath = Train("BDTS-GaribRath",770,450)
print(garibrath.getInfo())
print(garibrath.checkSeats())
print(garibrath.getFare())
garibrath.bookTicket()
print(garibrath.checkSeats())
print(garibrath.getFare())