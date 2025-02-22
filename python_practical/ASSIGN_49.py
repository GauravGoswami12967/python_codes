# Append text to a file and display the content
file_path = 'example.txt'

# Text to append
text_to_append = "This is the appended text.\n"

# Open the file in append mode
with open(file_path, 'a') as file:
    file.write(text_to_append)

# Read and display the content of the file
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
