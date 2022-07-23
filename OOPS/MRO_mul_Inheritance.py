class Car:
    def __init__(self,make,model,fuel):
        self.model = model
        self.make = make
        self.fuel = fuel

    def get_car_details(self):
        return "the make of the car is",self.make, "from car class"

class ElectricCar():
    def __init__(self, make, model, fuel):
        self.model = model
        self.make = make
        self.fuel = fuel

    def get_car_details(self):
        return "the make of the car is", self.make, "from ElectricCar class"

class Taxi(Car,ElectricCar):  # Multiple Inheritance
    def __init__(self, make, model, fuel):
        super(Taxi, self).__init__(make,model,fuel)

myobj = Taxi("tesla",2021,"electric")
print(myobj.get_car_details())
