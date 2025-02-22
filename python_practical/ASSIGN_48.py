# Define the file path
file_path = 'example.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the entire content of the file
    content = file.read()

# Print the content
print(content)
