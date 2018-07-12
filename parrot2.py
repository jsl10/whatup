#flag: acts as a signal of the program
"""
we can write our programs so they run while the flag is set to True and
stop running when any of several events sets the value of the flag to False.
while statement needs to check only one condition-- whether or not the flag is currently True.
"""

prompt="\nTell me somthing, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."

#set the program active state
active=True
#as long as active remins True, the loop will continue running
while active:
    message=input(prompt)

if message == 'quit':
    #set active False and while loop stop
    active=False
else:
    print(message)
