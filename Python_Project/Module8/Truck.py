import Automobile
class Truck(Automobile.Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        super().__init__(make,model,mileage,price)
        self.__drive_type=drive_type
    def set_drive_type(self,drive_type):
        self.__drive_type=drive_type

    def get_drive_type(self):
        return self.__drive_type
    
truck=Truck('Ashok_Leyland','T600 ADO','11','60000$','Right_Handed')
print("Manufacturer       -: ",truck.get_make())
print("Model Number       -: ",truck.get_model())
print("Mileage (in kmpl)  -: ",truck.get_mileage())
print("*Price             -: ",truck.get_price())
print("Driver Type        -: ",truck.get_drive_type())
