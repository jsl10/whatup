#input() function, python interprets everything the user enters as string.
age=input("How old are you? ")
#when we ask python for the value of age, it returns end-user's enter value
age
print('----') 

"""
when you try to use the input to do a numerical comparison, it store as string.
the enter value needs to be converted.
The int() function converts a string representation of a number
"""
age=int(age)
#python can run the conditional test. It compares age
a=age>=18
print(a)
print('----') 

