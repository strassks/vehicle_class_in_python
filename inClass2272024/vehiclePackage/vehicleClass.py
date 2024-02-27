'''
Vehicle Class
This class models a vehicle on a used car lot
change order: we need to add maximum speed to the model
change order: we need a way to read max speed from model
change order: some developers need to use the contructor without having to provide a max speed
'''
#constructor. its called when we instantiate an object of vehicle type
class Vehicle:
    def __init__(self, type, maxSpeed = None):
        '''
        parameter type is the kind of vehicle
        param: max speed of the vehicle, defaults to none
        
        '''
        self.type = type;
        self._thisIsPrivate = 42 #this is python data hiding 
        self.maxSpeed = maxSpeed
# a instance method. it operates on an instance of the vehicle class
    def printType(self):
        print(self.type);
    def getSpeed(self): #getter
        return self.maxSpeed
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass
