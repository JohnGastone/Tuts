# Specify the file name and mode ('w' for write)
file_name = "new_file.txt"

try:
    # Create a new file in write ('w') mode
    file = open(file_name, 'w')
    
    # Optionally, you can write data to the file
    file.write('Hello, World!')
    
    # Close the file to ensure proper resource management
    file.close()
    
    print(f'File "{file_name}" created successfully.')
except Exception as e:
    print(f'An exception occurred: {e}')
