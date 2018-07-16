#using a function with a while loop

def get_formatted_name(firstName, lastName):
    """Return a full name, neatly formatted."""
    fullName=firstName+' '+lastName
    return fullName.title()

#this is an infinite loop
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")

    fname=input("First name: ")
    if fname == 'q':
        break
    
    lname=input("Last name: ")
    if lname == 'q':
        break    

    formatted_name=get_formatted_name(fname, lname)
    print("\nHello, "+formatted_name+"!")
