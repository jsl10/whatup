#tuple looks just like a list except you use parentheses instead of square bracket
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
print("----")

#looping through all values in a tuple
for dimension in dimensions:
    print(dimension)
print("----")    

# Can't modify a tuple but you can assign a new value to variable that holds tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
print("----")

dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

