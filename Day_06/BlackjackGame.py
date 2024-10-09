import  random 
from Blackjack_art import logo

# create a deal_card() function that uses the list below to return random card
def deal_card():    # return a random card from deck
    cards = [11, 2, 3, 4, 5, 6,  7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    # cards = [1, 5, 3, 4]
    # return sum(cards)
    if sum(cards) == 21 and  len(cards) == 2:
       return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score ,  computer_score):
     if user_score == computer_score:
         return "Draw"
     elif computer_score == 0:
         return "Lose, opponent has BLACKJACK"
     elif user_score == 0:
         return "Win with a BLACKJACK"
     elif user_score > 21:
         return "You went over! You Lose"
     elif computer_score > 21:
         return "Opponent went over! You Win"
     elif user_score > computer_score:
         return "You Win!"
     else:
         return "You Lose!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # for user

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User's cards: {user_cards} and user's score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 and user_score > 21 :
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card and 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # for computer
            
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards} and final score: {user_score}")
    print(f"Computer's final hand is: {computer_cards} and final score: {computer_score}")
    print(compare(user_score , computer_score))

play_again = input("Do you want to play a BLACKJACK again? ( Type 'y' or 'n' ): ")
while play_again == 'y':
    print("\n"*5)
    play_game() 