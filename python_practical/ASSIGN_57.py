# Write a list to a file
file_path = 'example.txt'
my_list = ['apple', 'banana', 'cherry', 'date']

with open(file_path, 'w') as file:
    for item in my_list:
        file.write(f"{item}\n")

# Verify by reading and displaying the file content
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
