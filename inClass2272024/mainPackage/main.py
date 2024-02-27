from vehiclePackage.vehicleClass import *
if __name__ == "__main__":
    #instantiate an object if type vehicle 
    myCorvette = Vehicle("Car", 250) # trigger a call to constructor
    myCorvette.printType()#invoke the method on the object
    # invoke the getter
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed: ", maximum_speed)
    #instantiate another vehicle object 
    myRari = Vehicle("Fast car", 350)
    myRari.printType()
    maximum_speed = myRari.getSpeed()
    print("Maximum speed: ", maximum_speed)
    # list of 3 vehicles: car, boat, space ship
    myVehicles = [Vehicle("Uzi's Bugatti", 500), Vehicle("Lil Yachty's Yacht", 35), Vehicle("Elons Ship", 8000000)]
    for Vehicle in myVehicles:
        Vehicle.printType()
        print(Vehicle.getSpeed())