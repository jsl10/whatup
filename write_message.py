#Append

filename='programming.txt'

with open('programming.txt','a')as file_object:
    file_object.write("I also love finding meaning in large dataset\n")
    file_object.write("I love creating new apps that can run in a brower\n")

"""
You can open a file in read mode 'r'
write mode 'w'
append mode 'a'
or a mode that allows you to read and write to the file 'r+'
If you omit the mode argument, python opens the file in read only mode by default

"""
