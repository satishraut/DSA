
class Vehicle:
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioning,sunroof):
        # parent attribute
        Vehicle.make = make
        Vehicle.model = model
        Vehicle.fuel = fuel

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    def show_parent_attribute(self):
        print(Vehicle.make," ",Vehicle.model," ",Vehicle.fuel)

car = Car("Tesla","2021","Electric",True,True)

print(car.show_parent_attribute())