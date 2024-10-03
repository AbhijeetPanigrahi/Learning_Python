import random
from hangman_words import word_list 
from hangman_art import stages , logo
# word_list = [ "hulk" , "ironman" , "thor" ]



# step-1 :  (Picking a random word and checking answer)

# randomly choose a word from a list of words
# ask the user to uess the letter and assign the letter to a variable. Make guess lowecase
# check if the user guessed letter is in the chosen word. If yes, "right" else "wrong"

# Step-2 : Replacing blanks with spaces

# Create a placeholder with the same number of blanks as the chosen word
# Create a display that puts the guess letter in the right posintion in placeholder

# Step-3 : Checking if the user has won

# use a while loop to let the user guess the letter again
# Change the for loop so that we keep our prvious guess letters which are correct in display

# Step-4:

# create a variable called 'lives' to keep track of the number of lives left 
# Start lives = 6 
# If the guess letter is not in the choosen word then decrease the live by 1

print(logo)
lives = 6 


choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
for position in range(len(choosen_word)):
    placeholder += "_"
print(placeholder)   

# guess = input("Guess a letter: ").lower()
# print(guess)

# for letter in choosen_word:
#     if letter  == guess:
#         print("right")
#     else:
#         print("Wrong")



game_over  = False

correct_letters = [] 

# while(display != choosen_word):
while not game_over:
    print(f"********************* {lives} / 6 LIVES Left *********************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"******************* You have already guessed this letter {guess}. *******************")
    
    display =""
    for letter in choosen_word:
        if letter  == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:         # little doubt
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"*************************** The word is : {choosen_word}! You LOSE! **********************************")
    

    if "_" not in display:
        game_over = True
        print("*************************** You WIN! **********************************")

    print(stages[lives])
        
        
      




