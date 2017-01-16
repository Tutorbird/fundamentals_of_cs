# Nestor Alvarez, 20170116

import simplegui, random, math



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    # main game logic goes here 
    
    print "Guess was", guess

    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 300)



# register event handlers for control elements and start frame
frame.add_button("Range is 1K", range1000, 200)
frame.add_button("Range is 1C", range100, 200)
frame.add_input("Add a guess", input_guess, 200)
frame.start()


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
