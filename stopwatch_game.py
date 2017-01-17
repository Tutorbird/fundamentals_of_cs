# Nestor Alvarez, 20170116
import time, simplegui

# define global variables
deciseconds = 0
attempts = 0
score = 0
message = "0:00:0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def time_handler():
    global deciseconds
    deciseconds += 1
    print deciseconds
    return None

def draw_handler(canvas):
    scoreboard = "" +  str(score) + "/" + str(attempts) + ""
    canvas.draw_text(scoreboard, (200, 50), 20, 'Green')
    canvas.draw_text(message, (95, 110), 40, 'Red')

# define draw handler

    
# create frame


# register event handlers
frame = simplegui.create_frame("Stopwatch!", 300, 200)
timer = simplegui.create_timer(100, time_handler)
#frame.add_button("Click me", click)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
