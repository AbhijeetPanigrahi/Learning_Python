file = open("my_name.txt")
content = file.read()
print(content)
file.close()

# Instead of doing the above one always do like this :

with open("my_name.txt") as file:
    content = file.read()
    print(content)

with open("my_name.txt", mode='w') as file:     # write new text by removing the old one
    file.write("New Text")

with open("my_name.txt", mode='a') as file:     # append new text to the existing one
    file.write("\nNew Text 2")

with open("new_file.txt", mode='w') as file:     # create a new file if the file doesn't exist (work only in w mode)
    file.write("\nNew file created and wrote this text")
