# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

# You are going to create a list called result which contains the numbers that are common in both files. 

# e.g. if file1.txt contained: 

# 1 
# 2 
# 3

# and file2.txt contained: 

# 2
# 3
# 4


with open("file1.txt") as file1:
    new_file1 = [int(num.strip()) for num in file1.readlines()]
with open("file2.txt") as file2:
    new_file2 = [int(num.strip()) for num in file2.readlines()]
result = [num for num in new_file1 if num in new_file2]
print(result)