# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui, random, math

secret_number = 0
secret_range = 100
guesses = 0
message = "Welcome!"

# helper function to start and restart the game

def new_game():
    """ 
        Even though it doesn't matter in the given ranges
        We subtract one since the upper number is not
        included as a possible answer. [0. range)
    """
    global secret_number, guesses
    secret_number = random.randrange(0,secret_range)
    guesses = int(math.ceil(math.log(secret_range - 1) / math.log(2)))
    frame.set_draw_handler(draw)
    print "The range is 0 to", secret_range
    return None 

def decrement():
    global guesses
    guesses -= 1
    return None

def validate(guess):
    try:
        int(guess)
        return int(guess)
    except ValueError:
        print "Oops!  That was not a valid number.  Try again..."
    return None

def print_screen(flag, guess):
    # -1 is lower, 0 is equal, 1 is higher
    global message
    
    print "Guess was", guess
    print "Number of guesses left:", guesses
    
    if flag == -1:
        print "Lower!"
        message = "Lower!"
        
    elif flag == 0:
        print "Correct!"
        message = "Good Job!"
    elif flag == 1:
        print "Higher!"
        message = "Higher!"
    else:
        message = "Error!"
        print "Something weird happen. Our top coding monkeys are on it."
    frame.set_draw_handler(draw)
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

def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")
    
def input_guess(guess):
    # main game logic goes here 
    guess = validate(guess)
    if guess is not None:
        decrement()
        if guesses == -1:
            print "\nYou are out of guesses"
            print "Starting new game... \n"
            new_game()
        elif guess < secret_number:
            print_screen(1, guess)
        elif guess == secret_number:
            print_screen(0, guess)
        else:
            print_screen(-1, guess)

    
# create frame
frame = simplegui.create_frame("Guess the number!", 300, 200)



# register event handlers for control elements and start frame
frame.add_button("Range is 1K", range1000, 200)
frame.add_button("Range is 1C", range100, 200)
frame.add_input("Add a guess", input_guess, 200)
frame.start()


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
