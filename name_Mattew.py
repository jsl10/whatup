filename='annegreengables.txt'

with open('annegreengables.txt') as file_object:
    lines=file_object.readlines()

apple_string= ''
for line in lines:
    apple_string+=line.rstrip()

name=input("Enter Matthew: ")
if name in apple_string:
    print("Your name is Mattew")
else:
    print("You are not Mattew")

#we can check the name Matthew is contained in annegreengables.txt
