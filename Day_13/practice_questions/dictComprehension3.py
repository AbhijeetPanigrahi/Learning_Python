# You are given a string of text. Use dictionary comprehension to create a dictionary that counts the frequency of each word in the text, ignoring case.
# text = "Learning Python is fun. Learning Python is powerful."


text = "Learning Python is fun. Learning Python is powerful."
words = text.lower().replace('.', '').split()  # Convert to lowercase, remove punctuation, and split into words
word_count = {word: words.count(word) for word in set(words)}  # Use set to avoid duplicate keys
print(word_count)
