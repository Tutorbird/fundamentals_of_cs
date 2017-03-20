# Mini-project #6 - Blackjack

import simplegui, random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
result = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * 1, 
                    CARD_CENTER[1] + CARD_SIZE[1] * 0)
        
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []
        
    def __str__(self):
        # return a string representation of a hand
        cards_str = ""
        for card in self.cards:
               cards_str = " " + cards_str + str(card) + " | "
        return cards_str + "\n(Total = " + str(self.get_value()) + ")"
    
    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)        
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        aces = 0
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                aces += 1
                
        if (aces == 1) and (value + 10 <= 21):
            value += 10
            
        return value
   
    def draw(self, canvas, pos, hide):
        # draw a hand on the canvas, use the draw method for cards
        card_pos = pos
        
        if not hide:
            for card in self.cards:
                card.draw(canvas, card_pos)
                card_pos[0] += CARD_SIZE[0] /2
        else:
            card = self.cards[0]
            card.draw(canvas, card_pos)
            card_pos[0] += CARD_SIZE[0] / 2
            card.draw_back(canvas, card_pos)
                
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)
                
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        card = self.cards.pop()
        return card
    
    def __str__(self):
        # return a string representing the deck
        cards_str = ""
        for card in self.cards:
               cards_str += str(card)+" | "
        return cards_str

#define event handlers for buttons
def deal():
    global result, in_play, score
    global deck, player, dealer

    # your code goes here  
    if in_play:
        score -= 1
        
    result = ""
    in_play = True
    
    deck = Deck()
    deck.shuffle()

    dealer = Hand()
    player = Hand()

    # Turn-based
    card_dealt = deck.deal_card()
    dealer.add_card(card_dealt) 

    card_dealt = deck.deal_card()
    player.add_card(card_dealt)

    card_dealt = deck.deal_card()
    dealer.add_card(card_dealt) 

    card_dealt = deck.deal_card()
    player.add_card(card_dealt)
    
    # debug
    # print("Dealer Hand:" + str(dealer))
    # print("Player Hand:" + str(player))
    
def hit():
    # if the hand is in play, hit the player
    global result, in_play, score, deck, player

    if in_play:
        if (player.get_value() <= 21):
            card = deck.deal_card()
            player.add_card(card)

        if (player.get_value() > 21):
        # if busted, assign a message to result, update in_play and score
            result = "Bust! You lose!"
            in_play = False
            score -= 1

    # debug    
    # print("players:" + str(player))
    # print(result, in_play, score)
            
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global result, in_play, score, dealer
    if in_play:
        while dealer.get_value() < 17:
            card = deck.deal_card()
            dealer.add_card(card)
            
        if dealer.get_value() > 21:
            result = "Dealer busted! You won!"
            score += 1
        elif player.get_value() <= dealer.get_value():
            result = "You lost!"
            score -= 1
        else:
            result = "Winner! Winner! Chicken Dinner!"
            score += 1
            
        in_play = False
        
        # debug
        # print("Dealer Hand:" + str(dealer))
        # print("Player Hand:" + str(player))
        # print(result, in_play, score)
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [60, 100], 50, "Black")
    canvas.draw_text("Score: " + str(score), [400, 100], 30, "Black")
    
    canvas.draw_text("Dealer", [30, 170], 30, "Black")
    canvas.draw_text(result, [250, 270], 25, "Black")
    
    canvas.draw_text("Player", [30, 370], 30, "Black")
    player.draw(canvas, [30,400], False)
    if in_play:
        canvas.draw_text("Hit?", [300, 370], 40, "Black")
        dealer.draw(canvas, [30,200], True)
    else:
        canvas.draw_text("New deal?", [302, 372], 40, "Black")
        canvas.draw_text("New deal?", [300, 370], 40, "Red")
        dealer.draw(canvas, [30,200], False)
        


# initialization frame
frame = simplegui.create_frame("Blackjack", 700, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("New Game", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric