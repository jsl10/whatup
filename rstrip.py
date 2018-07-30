filename='annegreengables.txt'

with open('annegreengables.txt')as file_object:
    for line in file_object:
        print(line.rstrip())

#using rstrip() on each ine in the print statement eliminates these extra blank
