#passing a list
"""
when you pass a list to a function,
the function gets direct access to the contents of the list.
"""

def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title()+"!"
        print(msg)

#define a list of users and then pass the list usernames to greet_users() in our function
usernames=['hannah','ty','margot']
greet_users(usernames)

