#functions
"""
which are named blocks of code that are designed to do one specific job.
When you want to perform a particular task that you've defined in a function,
you call the name of the function responsible for it.
"""
#uses the keyword def to inform python that you're defining a function
def greet_user(): #the name of the function
    #docstrings are enclosed in triple quotes
    """Display a simple greeting."""
    #actual code in the body of function
    print("Hello!")

greet_user()
print('----')

def greet_user(username): #add function's definition: allow the function to aceept any value of username 
    """Display a simple greeting."""
    print("Hello!"+username.title()+"!")

#the function accepts the name you passes it and displays the greeting for the name
greet_user('jesse')
print('----')

"""
The variable username in the definition of greet_user() is an example of parameter,
a piece of information the function needs to do its job.
The value 'jesse' in greet_user('jesse') is an example of an argument.
An argument is a piece of information that is passed from a function call to a function.
when we call the function, place the value we want the function to work with parentheses.
In the argument 'jesse' was passed to the function greet_user()
"""
