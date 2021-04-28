# Classes provides means by which we bundle related data and functionalities together. it is a core aspect of object oriented programming, which is a programming paradigm that is based on the concepts of objects.

# Example of an object: car (properties; color, transmissio n type) (method; start-stop, accelerate)

# the things you can see are the properties

# functionality, actions of the properties

# basic terminologies
# attributes: refers to the properties affiliated with a given class e.g one of the attributes of car class is the colour
# methods: functions affiliated with some class
# instance: refers to the object created from calling the class.

# Creating Attributes

class Car:
    '''
    This is a car class

    '''

    def __init__(self, name, color):
        self.name = name
        self.color = color 

    def accel(self):
        print(f' The {self.color} {self.name} accelerates at 100mph')





car_1 = Car("mercedes", "silver")
car_2 = Car("benz", "blue")
print (car_1.accel())
car_2.accel()
# car_1.name = "mercedes"
# car_2.name = "benz"

print(car_1.color)
# print(car_2.name)


