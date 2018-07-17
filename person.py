#Returning a dictionary
"""
a function can return any kind of value you need it
"""
def buildPerson(firstName,lastName):
    """Return a dictionary of information about person."""
    person={'first':firstName,'last':lastName}
    return person
musician=buildPerson('hannah','montana')
print(musician)
print('----')
"""
the fuction build person() takes in a first and last name
and packs these values into dictionary: person={'first':firstName,'last':lastName}
"""
def buildPerson(firstName,lastName,age=''):
    """Return a dictionary of information about person."""
    person={'first':firstName,'last':lastName}
    if age:
        person['age']=age
        return person
    
musician=buildPerson('hannah','montana',age=10)
musician=buildPerson('john','jackson')
print(musician)
print('----')

"""
add a new optional parameter age to the functiondefinition and assign the parameter
an empty default value.
If the function call includes a value for this parameter,
the value is stored in the dictionary.
it can store more than person's name. you can modify information 
"""
