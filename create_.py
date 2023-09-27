# # Specify the file name and mode ('w' for write)
# file_name = "new_file.txt"

# try:
#     # Create a new file in write ('w') mode
#     file = open(file_name, 'w')

#     # Optionally, you can write data to the file
#     file.write('Hello, World!')

#     # Close the file to ensure proper resource management
#     file.close()

#     print(f'File "{file_name}" created successfully.')
# except Exception as e:
#     print(f'An exception occurred: {e}'
# )

import os
# Declare the file name
barua = "barua.pdf"

# Create the file barua.txt

file = open(barua, 'w')

# Write some data into the file barua.txt


file.write("Hii ni barua ya kirafiki kutoka \n kwa rafiki A kwenda kwa rafiki B")


# Delete a file barua.php

# os.remove("barua.php")

# Checking whether the file exists

if os.path.exists("barua.php"):
    print("This file do exists")
else:
    print("This file does not exist")


# Deleting a folder
# os.rmdir("folda")
