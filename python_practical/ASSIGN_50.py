# Read first n lines of a file
file_path = 'example.txt'
n = 5  # Number of lines to read

with open(file_path, 'r') as file:
    for _ in range(n):
        print(file.readline(), end="")
