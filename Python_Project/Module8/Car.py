import Automobile
class Car(Automobile.Automobile):
    def __init__(self,make,model,mileage,price,doors):
        super().__init__(make,model,mileage,price)
        self.__doors=doors
    def get_doors(self):
        return self.__doors
    def set_doors(self,doors):
        self.__doors=doors
        
car=Car('Tata','E250 CDI','15','40000$','4')
print("Manufacturer      -: ",car.get_make())
print("Model Number      -: ",car.get_model())
print("Mileage (in kmpl) -: ",car.get_mileage())
print("*Price            -: ",car.get_price())
print("Total Doors       -: ",car.get_doors())
        
