from art import logo
from os import system, name
import random

def deal_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card= random.choice(cards)
    return card
# define clear function
def clear():
   # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#Calculate score 
def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards)==21 and len(cards) == 2:
         return 0
      
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#Compare winner
def compare(user_score,comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, oppenent has a Blackjack"
    elif user_score == 0:
        return "Win, you got a Blackjack"
    elif user_score > 21:
        return "You went over, You Lose."
    elif comp_score > 21:
        return "Comp went over, You win "
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards=[]
    comp_cards=[]
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_a_card())
        comp_cards.append(deal_a_card())

    #Loop for user
    while not is_game_over:  
        user_score=calculate_score(user_cards)
        comp_score=calculate_score(comp_cards)
        print(f" Your cards: {user_cards}, current score {user_score}")
        print(f" Computer's first card: {comp_cards[0]}")
        

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over= True
        else:
            another_card=input("Would you like another card? Type 'y' for yes or 'n' to pass: ")
            if another_card == "y":
                user_cards.append(deal_a_card())
            else:
                is_game_over= True
    #Loop for computer
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_a_card())
        comp_score= calculate_score(comp_cards)
        #Check winner 
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
        print(compare(user_score, comp_score))

while input("Would you like to play a game of blackjack ? Type 'y' or 'n': ") == "y":
        clear()
        play_game()
   







