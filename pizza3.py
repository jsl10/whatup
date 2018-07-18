#using as to give a function as Alias
"""
you can use a short, unique alias, ex. make_pizza() = mp()
function make_pizza() an alias, mp(), by importing make_pizza as mp.
The as keyword renames a function using the alias you provide
"""

#rename the function make_pizza() to mp
#from module_name import function_name as fn
from pizza import make_pizza as mp

mp(16,'pepperoni')
mp(12,'mushromms','green peppers','extra cheese')



#using as to give a module an alias
#calling p.make_pizza() is more concisethan calling pizza.make_pizza():

#import module_name as mn
import pizza as p

p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushroom','green peppers','extra cheese')

"""
calling the functions by writing p.make_pizza() is not only more concise than
writing pizza.make_pizza(), but also redirects your attention from
the module name and allows you to focus on the descriptive names of its function.
"""

#importing all functions in a module
#tell python to import every function in module by using asterisk(*)

#from module_name import*
from pizza import*

make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')

"""
the asterisk in the import statement tells python to copy every function from
the module pizza into this program file.
because every function is imported, you can call each function by name without
using the dot notation.
However, it's best not to use this approach when you're working with larger module
that you didn't write.
"""


#styling functions
"""
every function should have a comment that explains concisely what the function does.
this comment should appear immediately after the function defintion
and use the docstring format
"""

#specify a default value for a parameter, no spaces should be used on either side of equal sign.
def function_name(parameter_0, parameter_1='default value')

#the same convention should be used for keyword arguments in function calls
function_name(value_0, parameter_1='value')

