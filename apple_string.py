filename='annegreengables.txt'

with open('annegreengables.txt') as file_object:
    lines=file_object.readlines()

apple_string= ''
for line in lines:
    apple_string+=line.rstrip()
print(apple_string)
print(len(apple_string))

#openning the file and storing each line of digits in a list
