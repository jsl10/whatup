filenmae='annegreengables.txt'

with open('annegreengables.txt')as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())
