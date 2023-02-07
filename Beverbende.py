# Beverbende CS101 Portfolio Project

# let's you play single player Beverbende against 1-4 Computer Players
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

# Additional: how will we make this cpu 'good'?

import random

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_link_node(self):
        return self.link_node

    def get_value(self):
        return self.value

class Stack:
  def __init__(self, name, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
    self.name = name
  
  def get_name(self):
    return self.name

  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the covered stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0

class Player:
  def __init__(self, name, cards=[], score=None):
    self.name = name
    self.cards = cards
    self.score = score

  def give_start_cards(self):
    new_cards = []
    
    for i in range(4):
      random_card = random.choice(deck)
      new_cards.append(random_card)
      deck.remove(random_card)

    self.cards = new_cards
  
  def draw_card(self):
    pass

  def trade(self):
    pass

  def score(self):
    score = 0

    for card in self.cards:
      if type(card) == str:
        score += 9
      else:
        score += int(card)
    
    return score

# Creating the BeverBende Deck
decknormal = 8*[0,1,2,3,4,5,6,7,8] + 9*[9]
deckspecial = 9*['Trade'] + 7*['Spy'] + 5*['Draw Twice']
decknormal.sort()
deck = decknormal + deckspecial

players = {}
uncovered = Stack('Uncovered', limit=len(deck))
covered = Stack('Covered', limit=len(deck))

# Enter number of Opponents
num_of_opp = int(input('Enter the number of opponents (1-4) for this game of Beverbende: '))
while num_of_opp < 1 or num_of_opp > 4:
    num_of_opp = int(input('Enter a number between 1 and 4: '))
    
# Creating the Player
name = input('Enter the name you want to play with: ')
player = Player(name)
players[player.name] = player

# Creating the oponents and adding them to Players dictionary
if num_of_opp == 1:
  cpu1 = Player('Opponent 1')
  players[cpu1.name] = cpu1
elif num_of_opp == 2:
  cpu1 = Player('Opponent 1')
  players[cpu1.name] = cpu1
  cpu2 = Player('Opponent 2')
  players[cpu2.name] = cpu2
elif num_of_opp == 3:
  cpu1 = Player('Opponent 1')
  players[cpu1.name] = cpu1
  cpu2 = Player('Opponent 2')
  players[cpu2.name] = cpu2
  cpu3 = Player('Opponent 3')
  players[cpu3.name] = cpu3
else:
  cpu1 = Player('Opponent 1')
  players[cpu1.name] = cpu1
  cpu2 = Player('Opponent 2')
  players[cpu2.name] = cpu2
  cpu3 = Player('Opponent 3')
  players[cpu3.name] = cpu3
  cpu4 = Player('Opponent 4')
  players[cpu4.name] = cpu4


# Giving each Player 4 random cards from deck
for player in players:
  players[player].give_start_cards()
  

# Create covered and uncovered stack and push remainder of deck on covered
for i in range(len(deck)):
  random_card = random.choice(deck)
  covered.push(random_card)
  deck.remove(random_card)

for player in players:
  print("{} has the following cards: {}, with a score of {} .".format(players[player].name, players[player].cards, players[player].score))

