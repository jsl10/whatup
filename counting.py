#using continue in a loop

"""
rather than breaking out of a loop entirely without executing the rest of its code,
you can use the continue statement to return to the beginning of the loop based on the result of
a conditional test.
"""

current_number=0
while current_number<10:
    #once inside the loop, increment the count by 1
    current_number+=1
    #if statement then check the modulo of current_number and 2
    if current_number%2==0:
        continue
    #if the current number is not divisible by2, the rest of the loop is executed and print
    print(current_number)
    print('----')


