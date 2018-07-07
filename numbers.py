#Print the numbers from 1 to 5, it doesn't print the number 5
for value in range(1,5):
    print(value)

print("----")

#Print the numbes from 1 to 6, it doesn't print the number6 
for value in range(1,6):
    print(value)

print("----")

#Using range() to make a list of numbers
"""
To make a list of numbers, you can convert the rsult of range() directly into a list
using the list() function.
Wrap list() around a call to the range() function.
"""

numbers=list(range(1,6))
print(numbers)
