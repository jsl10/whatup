#voting
age=19
if age>=18: # check to see whether the value in age is greater than or equal to 18
    print("You are lold enough to vote!")
    print("Have you registerd to vote yet?")
print('----')

#if-else
age=17
# if passes, the first block of indent print statements is executed
if age>=18:
    print("You are lold enough to vote!")
    print("Have you registerd to vote yet?")
#else, the second block of indent print statements is executed
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


#if-elif-else chain - it runs each conditional test in order until one passes
"""
admission for anyone under age 4 is free
admission for anyone between the ages of 4 and 18 is $5
admission for anyone age 18 or older is $10
"""
age=input("How old are you?")
if int(age)<4:
    print("Your admission cost is $0")
elif int(age)<18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")
print('----')

if int(age)<4:
    price=0
    print("Congrat! Your admission cost is $"+str(price)+".")
elif int(age)<18:
    price=5
    print("Well.. you are little old to get free admission. Please pay $"+str(price)+".")
else:
    price=10
    print("Wow! you are old. Pay me $"+str(price)+".")
print('----')    

if int(age)<4:
    price=0
    print("Congrat! Your admission cost is $"+str(price)+".")
elif int(age)<18:
    price=5
    print("Well.. you are little old to get free admission. Please pay $"+str(price)+".")
elif int(age)>50:
    price=8
    print("Senior discount. Pay me $"+str(price)+".")
else:
    price=10
    print("Wow! you are old. Pay me $"+str(price)+".")
