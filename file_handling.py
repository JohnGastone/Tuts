# File handling is a process that allows users to acess files and manipulate the files according to the granted privilleges

# File access : read(r), Write(w), Execute(x)

# FILE HANDLING in action

# Opening a file for reading

file = open('exceptions.py', 'r')

# Reading the file content

content = file.read()
print(content)

# Closing the file

file.close()


# Writing to a file

file = open('exceptions.py', 'w')
file.write("Hello Exceptions, you are realy confusing")

# Reading the file content

content = file.read()
print(content)
