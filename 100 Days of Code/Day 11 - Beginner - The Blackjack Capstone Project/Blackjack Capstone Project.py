from art import logo
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'no':")

should_continue = True

def deal_card():
    new_cards_list=[]
    new_cards_list.append(cards[random.randint(0,12)])
    return new_cards_list

deal_card()

user_cards = []
computer_cards = []

user_cards.append(random.randint(deal_card())*2)
computer_cards.append(random.randint(deal_card())*2)
print(user_cards)
print(computer_cards)


some_list = []

def calculate_score():
    for x in some_list:
        the_score = sum(x)
        if the_score == 21:
            print(the_score)
calculate_score()



print()