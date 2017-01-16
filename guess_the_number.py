# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random, math

secret_number = 0
secret_range = 100
guesses = 0

# helper function to start and restart the game
def decrement():
    global guesses
    guesses -= 1
    return None

def new_game():
    """ 
        Even though it doesn't matter in the given ranges
        We subtract one since the upper number is not
        included as a possible answer. [0. range)
    """
    global secret_number, guesses
    secret_number = random.randrange(0,secret_range)
    guesses = int(math.ceil(math.log(secret_range - 1) / math.log(2)))
    return None    

# define event handlers for control panel
def range100():
    global secret_range 
    secret_range = 100
    new_game()
    return None

def range1000():
    global secret_range 
    secret_range = 1000
    new_game()
    return None
    
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
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random, math

secret_number = 0
secret_range = 100
guesses = 0

# helper function to start and restart the game
def decrement():
    global guesses
    guesses -= 1
    return None

def new_game():
    """ 
        Even though it doesn't matter in the given ranges
        We subtract one since the upper number is not
        included as a possible answer. [0. range)
    """
    global secret_number, guesses
    secret_number = random.randrange(0,secret_range)
    guesses = int(math.ceil(math.log(secret_range - 1) / math.log(2)))
    return None    

# define event handlers for control panel
def range100():
    global secret_range 
    secret_range = 100
    new_game()
    return None

def range1000():
    global secret_range 
    secret_range = 1000
    new_game()
    return None
    
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
