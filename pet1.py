#Default values
"""
you can define a defualt value for each parameter.
using defualt values can simplify your function calls
and clarify the ways in which your funtions are typically used.

def describe_pet(pet_name,animal_type='dog'): #provide an animal type and name
    """Display information about a pet"""
    print("\nIhave a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet(pet_name='willie')
print('----')


Note that the order of the parameters in the function definition had to be changed.
Because the defualt value makes it unnecessary to specify a type of animal as an argument,
the only argument left in the function call is the pet's name.
Python still interprets this as positional argument,
so if the function is called with just a pet's name,
that argumetn will match up with the first parameter listed in function's definition.
"""

#equivalent function calls: all of the following calls would work for this function
#a dog named willie
describe_pet('willie')
describe_pet(pet_name='willie')

#a hamster named Harry
describe_pet('harry','hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


#avoiding argument errors
"""
When you start to use functions, don't be surprised if you encounter errors about unmatched arguements.
unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.
"""

