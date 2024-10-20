#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./Input/Names/invited_names.txt", 'r') as invited_names:
    # print(invited_names.readlines())
    names_list = invited_names.readlines()
    names_list = [name.strip() for name in names_list]

    for name in names_list:
        with open(f"D:/Learning_Python/Day_11/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", 'w') as new_letter:
            with open("D:/Learning_Python/Day_11/Mail Merge Project Start/Input/Letters/starting_letter.txt", 'r') as starting_letter:
                for line in starting_letter:
                    new_letter.write(line.replace('[name]', name))
