# Read last n lines of a file
file_path = 'example.txt'
n = 5  # Number of lines to read from the end

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end="")
