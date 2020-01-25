import Automobile
class SUV(Automobile.Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        super().__init__(make,model,mileage,price)
        self.__pass_cap=pass_cap
    def set_pass_cap(self,pass_cap):
        self.__pass_cap=pass_cap

    def get_pass_cap(self):
        return self.__pass_cap
    
suv=SUV('Mahindra','S500 MAH','18','40000$','None')
print("Manufacturer       -: ",suv.get_make())
print("Model Number       -: ",suv.get_model())
print("Mileage (in kmpl)  -: ",suv.get_mileage())
print("*Price             -: ",suv.get_price())
print("Pass Cap           -: ",suv.get_pass_cap())
