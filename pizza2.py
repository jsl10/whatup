#mixing positional and arbitrary arguments
"""
accept several different kinds of arguments,
the parameter that accepts an arbitrary number of arguments must be placed
last in the function definition.
python matches positional and keyword arguements first and then collect
any remaining arguments in the final parameter
"""

#function calls include an argumentfor the size first, followed by as many topping as needed
def make_pizza(size,*toppings):
    """summarize the pizza we are about to make"""
    print("\nMaking a "+str(size)+
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
    print('----')

#now each pizza has a size and a number of toppings
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
