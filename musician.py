#making an argument optional

#with middle name
"""
you can use default values to make an argument optional
"""

def get_formatted_name(firstName,middleName,lastName):
    """Rturn a full name, neatly formatted."""
    fullName=firstName+' '+middleName+' '+lastName
    return fullName.title()
musician=get_formatted_name('justin','awsome','timberlake')
print(musician)
print('----')

#without middle name

#name is built from three posible parts.
"""
first and last name: these parameters are listed first in function definition.
middle name is optional: listed last in the definition, default value is an empty string
"""
def get_formatted_name(firstName,lastName,middleName=''):
    """Rturn a full name, neatly formatted."""
    if middleName:
        fullName=firstName+' '+middleName+' '+lastName
    else:
        fullName=firstName+' '+lastName
        return fullName.title()

musician=get_formatted_name('Fiona','Apple')
print(musician)
print('----')

musician=get_formatted_name('James','Alexander','Kindermander')
