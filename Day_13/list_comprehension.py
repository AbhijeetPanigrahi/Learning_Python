# new_numbers = [new_item for item in list]
# new_numbers = [new_item for item in list if test]
# ( remember the above two syntax ) ☝️
# EXAMPLE:-

numbers = [1,2,3]
new_numbers = []
for n in numbers:
    n += 1
    new_numbers.append(n)

print(new_numbers) # Output: [2, 3, 4]

# Using list comprehension ( here 'list' = 'numbers' and 'item' = 'n' and 'new_item' = n + 1)

new_numbers = [n+1 for n in numbers]
print(new_numbers)

# You can do it also for STRINGS

name = "Abhijeet"
letters_list = [letter for letter in name]
print(letters_list) # ['A', 'b', 'h', 'i', 'j', 'e', 'e', 't']

# You can also use list comprehension with conditionals

numbers = [1,2,3,4,5,6]
even_numbers = [n for n in numbers if n % 2 == 0]   # remember the syntax
print(even_numbers) # Output: [2, 4, 6]

# You can also use list comprehension with multiple conditions