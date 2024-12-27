class bike:
    def __init__(self , make, colorr):
        self.make = make
        self.colorr = colorr
    def color(self):
        print(f"i am parent class{self.make} {self.colorr}")

bikeone = bike(2222, "red")



#  inheritance

class ebike(bike):
    def __init__(self, make , battery):
        super().__init__(make , colorr="green")
        self.battery = battery
        
      #overiding a parent method 
    def color(self):
        print(f"{self.make} {self.battery}")
        
ebikeone = ebike(4444, "7 kvh")
ebikeone.color()