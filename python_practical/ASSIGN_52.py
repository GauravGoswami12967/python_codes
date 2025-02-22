# Read file line by line and store it into a list
file_path = 'example.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

print(lines)  # List containing all lines
