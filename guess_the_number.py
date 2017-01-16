# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random, math

secret_number = 0
secret_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,secret_range)
    
    print "Range", secret_range, "| Number", secret_number

# define event handlers for control panel
def range100():
    global secret_range 
    secret_range = 100
    new_game()
    print "Range changed to 100"

def range1000():
    global secret_range 
    secret_range = 1000
    new_game()
    print "Range changed to 100"
    
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
