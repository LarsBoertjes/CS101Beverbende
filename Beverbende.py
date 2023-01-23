# Beverbende CS101 Portfolio Project

# let's you play single player Beverbende against 2 or more Computer Players
# You will see 4 uncovered values on your screen which represent your cards with a value
# (first make it while you see the cards, later make it hidden)
# You will see the 2 outside cards for a very brief moment
# There are two stacks of cards, one covered, one uncovered.

# Option A: player takes from covered stack
# Option: it is a normal card, player choses to trade with one of his own cards, or put the card on the uncovered stack
# Option: it is a special card, player choses to use the special card with its action, or put the card on the uncovered stack

# Option B: player takes from uncovered stack
# Player has to trade card with one of his 4 own card, choses himself which one

# Special Cards:
# Trade: player who draws this card can trade against one of other players cards
# Look: player can look up the value of one of his 4 cards
# Draw Twice: Gets to draw, if player doesn't want the card, he can draw again.

# Game goes on until 1 player calls 'last round', then; every other player gets to play one more round
# After this round, cards have to be shown. 
# Score is calculated by value of normal cards.
# If there are still special cards belonging to a player, the player must trade them with the top card on the uncovered stack

# Steps:
# Build deck
# Assign 4 random cards from deck to every player
# Uncover 4 random cards

import random

decknormal = 8*[0,1,2,3,4,5,6,7,8] + 9*[9]
deckspecial = 9*['Trade'] + 7*['Spy'] + 5*['Draw Twice']
decknormal.sort()
deck = decknormal + deckspecial

class Player:
    def __init__(self, name, cards=[None, None, None, None], score=None):
        self.name = name
        self.cards = cards
        self.score = score

    def draw_card(self):
        pass

Lars = Player('Lars Boertjes')

# Assign Players
num_of_players = int(input('Enter the number of players (2-4) for this game of Beverbende: '))

if num_of_players < 2 or num_of_players > 4:
    print('Enter a number between 2 and 4')

name = input('Enter the name you want to play with: ')

player = Player(name, [deck[random.randint(0, len(deck))] for value in range(4)])


# Print player.cards
print(player.name)
print(player.cards)

