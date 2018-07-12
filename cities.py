"""
to exit a while loop immedicately without running any remaining code in the loop,
regardless of the result of any conditional test,
use the break statement
Break statement directs the flow of your program
You can use it to control which line of code are exwecuted and which aren't
"""
prompt="\nPlease enter the name of a city you have visited:"
prompt+="\n(Enter 'quit' when you are finished.)"

while True:
    city=input(prompt)

    if city == 'quit':
        break #a loop that starts with while True will run forever unless it reaches a break
    else:
        print("I'd love to go to "+city.title()+"!")

