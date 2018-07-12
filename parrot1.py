#Letting the user choose when to quit
"""
It will define a quit value and then keep the program running
as long as the user has not entered the quit value
"""

prompt="\nTell me somthing, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
#message stores whatever value that end-user entered
message=""
while message != 'quit':
    message=input(prompt)
    print(message)
    #if it doesn't not match the quit value
    if message != 'quit':
        print(message)
