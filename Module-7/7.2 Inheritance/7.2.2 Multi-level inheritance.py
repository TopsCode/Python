# multi-level inheritance
class Drive:  
    def drive(self):  
        print("Drive safe")  

class Vehical(Drive):  
    def onRoad(self):  
        print("Vehical")  

class Car(Vehical):  
    def car_drive(self):  
        print("Car")  

obj=Car()
obj.drive()
obj.car_drive()
obj.onRoad()