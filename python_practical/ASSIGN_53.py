# Read file line by line and store it into a variable
file_path = 'example.txt'
content = ""

with open(file_path, 'r') as file:
    for line in file:
        content += line

print(content)  # Entire content of the file stored in 'content'
