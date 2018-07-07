#testing multiple conditions
#check to see whether topping requested
requested_toppings=['mushrooms','extra cheese','green peppers']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nfinished making your pizza!")
print('----')

if 'mushrooms' in requested_toppings: # mushroom passed
    print("Adding mushrooms")
#once if passed, it doens't run any test beyond the first test that passes    
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nfinished making your pizza!")
print('----')


#Using if statemnet with list
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")
print('----')

#If pizzaria runs out of green peppers?
#if statement inside the for loop
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping+".")
print('----')

#checking that a list is not empty
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings: #do quick check
        print("Adding "+requested_topping+".")
    print("n\Finished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")
print('----')    

#using multiple list
a_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
r_toppings=['mushrooms','french fries','extra cheese']
#for loop through the list of requested_toppings and check to see if each requested topping is available
for r_topping in r_toppings:
    #if it is, add that topping to the pizza     
    if r_topping in a_toppings:
        print("Adding "+r_topping+".")
    #else block running if requested topping is not in the list of available topping    
    else:
        print("Sorry, we don't have "+r_topping+".")
print("\nFinished making your pizza!")
print('----')

#helloAdmin
name=input("What's your name: ")
role=input("Type your role: ")

if role == 'admin':
    print("Hello "+name.title()+" "+role.title())
else:
    print("Who are you?")



