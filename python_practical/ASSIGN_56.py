# Count the frequency of words in a file
file_path = 'example.txt'

with open(file_path, 'r') as file:
    text = file.read().lower()  # Convert text to lowercase for case-insensitive counting
    words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
