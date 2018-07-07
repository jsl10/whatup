# Forgetting to indent additional lines
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick!")

print("I can't wait to see your next trick, "+magician.title()+".\n")

"""
The last statement is supposed to be indented, but because python finds at least
one indented line after the for statement, it doesn't report an error.
The first print statement is exuted once for each name in the list
because it is indented.
The second print statement is not indented, so it's excuted only once after
the loop has finished running.

This is a logical error. The syntax is valid Python code, but the code does not
produce the desired result because a problem occurs in its logic.

"""
