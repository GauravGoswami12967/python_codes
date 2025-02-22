# Find the longest word in a file
file_path = 'example.txt'

with open(file_path, 'r') as file:
    words = file.read().split()

longest_word = max(words, key=len)
print("The longest word is:", longest_word)
