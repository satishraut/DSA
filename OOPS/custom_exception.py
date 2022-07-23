class NegetiveCarValue(Exception):
    def __init__(self, value,message="car value should not be negative"):
        self.value = value
        self.message = message
        super().__init__(self.message) # put message into the parent class

    def __str__(self):
        return f"{self.message}----->{self.value}"
a = 1
if a<3:
    raise NegetiveCarValue(a) #NegetiveCarValue: car value should not be negative----->1