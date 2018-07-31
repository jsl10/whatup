#writing to an empty file

filename='programming.txt'

with open('programming.txt','w')as file_object:
    file_object.write("I love programming")
    file_object.write("I love creating new games")
    file_object.write("I love programming\n")
    file_object.write("I love creating new games\n")



"""
You can open a file in read mode 'r'
write mode 'w'
append mode 'a'
or a mode that allows you to read and write to the file 'r+'
If you omit the mode argument, python opens the file in read only mode by default

"""
