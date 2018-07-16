#passing an arbitrary number of arguments
"""
Python allows a function to collect an arbitrary number of arguments from the calling statement
"""

#one parameter=*toppings, but this parameter collects as many arguments as the calling line provides
def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print(toppings)
    print('----')

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


"""
The asterisk in the parameter name *toppings tells python to make an empty tuple
called toppings and pack whatever values it receives into this tuple.
the print statement in the function body produces output showing
that python can handle a function call with one value and a call with three value
"""

def make_pizza(*toppings):
    """summerize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- "+topping)
    print('----')

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
