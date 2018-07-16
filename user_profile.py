#using arbitrary keyword arguments
"""
you can write functions that accept
as many key-value pairs as the calling statement provides
"""


"""
the definition of build_profile() expects a first and last name, and then it allows
the user to pass in as many name-value pairs as they want.
doulble asterisks(**userInfo): python to create an empty dictionary called userInfo
and pack whatever name-value pairs it receives into this dictionary.
"""
def build_profile(first,last,**userInfo):
    """"Build a dictionary containing everything we know about a user."""
    #empty dictionary to hold the user's profile.
    profile={}
    profile['firstName']=first
    profile['lastName']=last

    """loop though the additional key-value pairs in the dictionary userInfo and add each pair to the profile dictionary."""
    for key, value in userInfo.items():
        profile[key]=value
    return profile

userProfile=build_profile('albert','einstein',
                         location='princeton',
                         field='physics')
print(userProfile)
