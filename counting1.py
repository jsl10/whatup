#avoiding infinite loops
x=1
while x<= 5:
    print(x)
    x+=1
"""
If you accidentlly omit the line x+=1, the loop will run forever.
In this case, the vlaue of x will start at 1 but never change.
the conditional test x<=5 will always evaluate to True
and the while loop will run forever.
"""
