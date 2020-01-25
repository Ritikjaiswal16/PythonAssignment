import random
class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f'a {self.color} car which gave mileage of {self.mileage}kmpl'
mile=random.randint(10,25)
a=random.randint(0,3)
d={0:'RED',1:'BLACK',2:'BLUE',3:'YELLOW'}
color=d[a]
print(Car(color,mile))
