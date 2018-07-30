#classes
class Car():
    """A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        """initialize attributes to describe a car"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """return a neatly formatted descripve name"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    #method that makes it easy to read a car's mileage 
    def read_odometer(self):
        """print a statement showing the car's mileasge"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        """
        set the odometer reading to the given value
        reject the change if it attempts to roll the odometer back.
        """
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(10)
my_new_car.read_odometer()


"""
modify value 3ways.
1. you can change directly through an instance
2. set the value through a method
3. increment the value(add a certain amount to it) through a method
"""
