#upper case
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=="bmw":
        print(car.upper())
    else:
        print(car.title())

print('----')

"""
Conditional tests
if statement is an expression that can be evaluated as True or False
and is called a conditional test.
"""
#this equality operation returns True if match, False if they don't match
print(car=='bmw')
print(car.lower()=='audi')



