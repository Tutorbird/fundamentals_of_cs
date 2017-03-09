# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck
    deck = range(0,8)
    deck.extend(deck)
    random.shuffle(deck)
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    count = 1
    for n in deck: 
        canvas.draw_text(" " + str(n), (count * 45, 75), 80, "Red")
        count += 1
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric