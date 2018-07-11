#dictionary in a dictionary
"""
you can nest a dictionary inside dictionary, but your code can ge complicated quickly
"""
#define a dictionary called user with two keys
#each key is a dictionary that includes each user's first, last name and location
users={
    'aeinstein':{
        'first':'albert', 
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
#loop through the users dictionary
for username, user_info in users.items():
#once inside the main dictionary loop, print the username
    print("\nUsername: "+username)
#start accessing the inner dictionary    
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']

#print a summary of what we know about each user
    print("\tFull name:"+full_name.title())
    print("\tLocation: "+location.title())
print('----')


