number=input("Enter a number, and I'll tell you if it's even or odd: ")
number=int(number)

#even numbers are always divisible by two
if number%2 == 0:
    print("\nThe number "+str(number)+"is even.")
else:
    print("\nThe number "+str(number)+" is odd.")
