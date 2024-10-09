# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

# print(
# '''

# ░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
# ░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
# ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀

# ''')
# direction = input("Type 'Encode' for encoding and type 'Decode' for decoding. \n").lower()
# text = input("type your message: \n").lower()
# shift = int(input("Type the shift number\n"))

# def caeser(original_message, shift_amount, encode_or_decode):
#     output_text = ""
#     if encode_or_decode == "decode":
#         shift_amount *= -1
#     for letter in original_message:
#         if letter not in alphabet:  # Check if letter is in alphabet
#             output_text += letter
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position = shifted_position % len(alphabet)  # 0 - 25 range
#             output_text += alphabet[shifted_position]
#     print(f"Here is your {encode_or_decode}d result: {output_text}")

# caeser(text, shift, direction)


print('''
░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀
''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_message, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print(f"Here is your {encode_or_decode}d result: {output_text}")

while True:
    direction = input("Type 'Encode' for encoding and type 'Decode' for decoding. \n").lower()
    text = input("type your message: \n").lower()
    shift = int(input("Type the shift number\n"))

    caeser(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    if restart != 'yes':
        print("Goodbye!")
        break