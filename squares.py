"""
1.start with empty list called squares
2.python loop through each value from 1 to 10 using the range() function
3.the current value is raised to the second power and stored in the variable square
4.each new value of square is appended to the list squares.
"""

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)


print ("----")

"""
to write this code more considely, omit the temporary variable square and
append each new avlue directly to the list
"""
# each value in the loop is raised to the second power and then immediately appended to the list of squares.
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

print("----")

#list comprehension allows you to generate this same list in just one line of code
squares=[value**2 for value in range(1,11)]
print(squares)

