# Doing something after a for loop

magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick, "+ magician.title()+".\n")

print("Thank you, everyone. That was a great magic show!")

"""
The first two print states are repeated once for each magician in the list.
Last line, because the line is not indented, it's printed only once.
"""
