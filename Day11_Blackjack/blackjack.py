#!/usr/bin/env python
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
from art import logo
#from replit import clear

# 2 to 10, jack, queen, king, ace
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

'''This is the Capstone Project "Blackjack" from Angela Yu\'s
"100 days of code" Python course.''' 

def get_deck(num=2):
  '''Get cards for one player. Return a list.'''
  deck = []
  for _ in range(num):
    deck.append(random.choice(cards))
  return deck

def get_score(deck):
  '''Count and return the score for the given deck.
  Switch score for one ace from 11 to 1 if total score
  exceeds 21.'''
  score = sum(deck)
  if score > 21 and 11 in deck:
    score -= 10
  return score    

def is_blackjack(deck):
  '''Return True/False if the deck is a blackjack,
  i.e., if the deck contains exactly one ace and
  one card valued at 10.'''
  if len(deck) == 2 and 10 in deck and 11 in deck:
    return True
  else:
    return False
    
def show_decks_partially(deck_player, deck_dealer):
  '''Show full deck of player along with score.
  Show only the first card of the computer/dealer.'''
  print(f'Your cards: {deck_player}, current score: {get_score(deck_player)}')
  print(f"Computer's first card: {deck_dealer[0]}")

def show_decks_fully(deck_player, deck_dealer):
  '''Show full decks of player and dealer along with their scores.'''
  print(f'Your final hand: {deck_player}, final score: {get_score(deck_player)}')
  print(f"Computer's final hand: {deck_dealer}, final score: {get_score(deck_dealer)}")

def players_turn(deck_player, deck_dealer):
  '''Execute the player\'s round. Finish when they do not want
  another card or their score exceeds 21.'''
  while True:
    show_decks_partially(deck_player, deck_dealer)
    answer = input("Type 'y' to get another card, type 'n' to pass: ")
    if answer != 'y':
      break
    deck_player.append(random.choice(cards))
    if get_score(deck_player) >= 21:
      break
  return deck_player

def dealers_turn(deck_player, deck_dealer):
  '''Execute the dealer\'s round. Dealer must have at least 17
  points.''' 
  score_player = get_score(deck_player)
  score_dealer = get_score(deck_dealer)
  while score_dealer < 17:
    deck_dealer.append(random.choice(cards))
    score_dealer = get_score(deck_dealer)
  return deck_dealer

def determine_winner(deck_player, deck_dealer):
  '''Determine who won the game and show an
  appropriate message.'''
  score_player = get_score(deck_player)
  score_dealer = get_score(deck_dealer)
  if is_blackjack(deck_dealer):
    print("Computer has blackjack. You lose.")
  elif is_blackjack(deck_player):
    print("Blackjack! You win.")
  elif score_player > 21:
    print("You went over. You lose.")
  elif score_player == score_dealer:
    print("It's a draw!")
  elif score_dealer > 21:
    print("Opponent went over. You win.")
  elif score_dealer < score_player:
    print("You win.")
  else:
    print("You lose.")
  
def blackjack_round():
  '''Execute one round of Blackjack.'''
  #clear()
  print(logo)
  deck_player = get_deck()
  deck_dealer = get_deck()
  if (not is_blackjack(deck_player) and 
      not is_blackjack(deck_dealer)):
    deck_player = players_turn(deck_player, deck_dealer)
    if get_score(deck_player) < 22:
      deck_dealer = dealers_turn(deck_player, deck_dealer)
  show_decks_fully(deck_player, deck_dealer)
  determine_winner(deck_player, deck_dealer)

if __name__ == '__main__':
  answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  while answer == 'y':
    blackjack_round()
    answer = input('Do you want to play a round of Blackjack? (y/n): ')
  
  print('Thanks for playing! Good-bye!')
