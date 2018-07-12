"""
we used remove() to remove a specific value from a list
the remove() function worked because the value we were interested in appeard only once in the list
"""
#to remove all instances of that value, run a while loop until 'cat' is no longer in the list
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

"""
once inside the loop, python removes the first instance of 'cat', return to the while line,
and then reenters the loop when it finds that 'cat' is still in the list.
It removes each instance of 'cat' until the value is no longer in the list.
"""
