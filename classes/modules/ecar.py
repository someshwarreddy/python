import car

class ecar(car.Car):
    def __init__(self, type , battery):
        super().__init__(type)
        self.battery = battery
    
    def havebattery(self):
        print(self.battery, self.cartype)

ecar = ecar("ecar tesla" , "100kvh")
ecar.havebattery()
