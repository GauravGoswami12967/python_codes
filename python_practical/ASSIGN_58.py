# Copy the contents of a file to another file
source_file_path = 'source.txt'
destination_file_path = 'destination.txt'

with open(source_file_path, 'r') as source_file:
    content = source_file.read()

with open(destination_file_path, 'w') as destination_file:
    destination_file.write(content)

print(f"Content copied from {source_file_path} to {destination_file_path}")
