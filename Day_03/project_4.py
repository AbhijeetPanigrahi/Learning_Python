import string
import random

# Array of all alphabets (lowercase and uppercase)
letters = list(string.ascii_letters)  # 'a' to 'z' and 'A' to 'Z'

# Array of numbers from 0-9
numbers = list(string.digits)  # '0' to '9'

# Array of common symbols
symbols = list("!@#$%^&*()_+-=[]{}|;:'\",.<>?/~`")

print("\nWelcome to the password generator\n")

nr_letters = int(input("Enter number of letters would you like?\n"))
nr_symbols = int(input("Enter number of symbols would you like?\n"))
nr_numbers = int(input("Enter number of numbers would you like?\n"))


# Easy Level

password_easy = ""

for char in range(0, nr_letters):
    password_easy += random.choice(letters)

for symb in range(0, nr_symbols):
    password_easy += random.choice(symbols)

for num in range(0, nr_numbers):
    password_easy += random.choice(numbers)

print(f"\nYour easy password: {password_easy}\n")

# Hard Level    (Completely random order)

password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))    #  password_list += random.choice(letters)

for symb in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)
# print(password_list)

password_hard = ""
for char in password_list:
    password_hard += char

print(f"Your hard password: {password_hard}\n")