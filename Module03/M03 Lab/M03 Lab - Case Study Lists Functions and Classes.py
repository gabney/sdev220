"""
Module 03 Lab - Case Study: Lists, Functions, and Classes
SDEV 220
Gabriel Abney

This program for the Module 03 Lab creates a superclass called Vehicle and \
a subclass called Automobile with additional attributes.  The program also \
collects user input about a specific car to be created as an object, and then \
prints the details of the created object back to the user.  The Vehicle class \
has the 'type' attribute, and the Automobile class has the attributes 'year',  \
'make', 'model', 'doors', and 'roof' which are input upon initialization.
"""

# defines the Vehicle class

class Vehicle():
    def __init__(self, type):
        self.type = type


# defines the Automobile class
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type) #inherits 'type' attribute from Vehicle superclass
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def details(self):
        print(f"The description of your vehicle is:\
              \nVehicle type: {self.type}\
              \nVehicle year: {self.year}\
              \nVehicle make: {self.make}\
              \nVehicle model: {self.model}\
              \nVehicle doors: {self.doors}\
              \nVehicle roof: {self.roof}")


#main program body
print("Welcome to ACME vehicle registry.")

#questions to ask the program user
q1 = input("Please input your vehicle type: ")
q2 = input("Please input your vehicle's year: ")
q3 = input("Please input your vehicle's make: ")
q4 = input("Please input your vehicle's model: ")
q5 = input("Please input your vehicle's number of doors: ")
q6 = input("Please input your vehicle's roof type: ")

#generates the custom vehicle from user inputs
custom_vehicle = Automobile(q1,q2,q3,q4,q5,q6)

#prints custom vehicle details from attributes of the object
custom_vehicle.details()