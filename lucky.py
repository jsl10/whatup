while True:
    try:
        a=int(input("Guess your lucky number? "))
    except ValueError:
        print ("Please do something!")
        continue
    else:
        break
if a <= 5:
    print ("Oh well.. Let's try again")
else:
    print ("You got lucky day! ")
