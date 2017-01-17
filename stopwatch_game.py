# Nestor Alvarez, 20170116
import time, simplegui

# define global variables
deciseconds = 0
attempts = 0
score = 0
message = "0:00:00"
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    # Seconds = decisecond / 10
    # Minutes = seconds / 60
    tenths = deciseconds % 10
    secs = (deciseconds // 10) % 60
    mins = (deciseconds // 600) % 60
    return "%d:%02d:%02d" % (mins, secs, tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    if stopped:
        stopped = False
        timer.start()

def stop():
    global stopped, attempts, score
    if not stopped:
        timer.stop()
        stopped = True
        attempts += 1
        if (deciseconds % 10 == 0):
            score += 1

def reset():
    global stopped, attempts, score, deciseconds, message
    stopped = True
    message = "0:00:00"
    timer.stop()
    attempts =  score = deciseconds = 0

# define event handler for timer with 0.1 sec interval
def time_handler():
    global deciseconds
    global message
    deciseconds += 1
    message = format(deciseconds)
    return None

# define draw handler
def draw_handler(canvas):
    scoreboard = "%d/%d" % (score, attempts)
    canvas.draw_text(scoreboard, (200, 50), 20, 'Green')
    canvas.draw_text(message, (95, 110), 40, 'Red')
    
# create frame
frame = simplegui.create_frame("Stopwatch!", 300, 200)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# register event handlers
timer = simplegui.create_timer(100, time_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
