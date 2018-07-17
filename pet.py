"""
because a function definition can have multiple parameter,
a function call may need multiple arguments
positional arguments: which need to be in the same order the parameters were written
keyword arguments: each argument consists of a variable name and a value
"""


#python must match each argument in the function call with a parameter in the function definition
def describe_pet(animal_type, pet_name): #provide an animal type and name
    """Display information about a pet"""
    print("\nIhave a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('hamster','harry')
#multiple function calls
describe_pet('dog','willie')
describe_pet('cat','ocean')
print('----')

def describe_pet(animal_type, pet_name): #provide an animal type and name
    """Display information about a pet"""
    print("\nIhave a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet(animal_type='hamster',pet_name='harry')
#python knows where each value should go.
describe_pet(pet_name='harry',animal_type='hamster')
print('----')
