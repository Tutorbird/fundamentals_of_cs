# Implementation of classic arcade game Pong
import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
RIGHT = True
LEFT = False
BALL_POS = [WIDTH / 2 , HEIGHT / 2]
BALL_VEL = [random.randrange(60, 180) / 60, random.randrange(120, 240) / 60]
SCORE_ONE = 0
SCORE_TWO = 0
PADDLE1_POS = HEIGHT / 2
PADDLE2_POS = HEIGHT / 2
PADDLE1_VEL = 0
PADDLE2_VEL = 0
VEL_MULTIPLIER = 1.1
    
def spawn_ball(DIRECTION):
    global BALL_POS, BALL_VEL
    
    BALL_POS = [WIDTH / 2 , HEIGHT / 2]
    BALL_VEL[1] = -random.randrange(60, 180) / 60    
    if DIRECTION == RIGHT:
        BALL_VEL[0] = random.randrange(120, 240) / 60
    else:
        BALL_VEL[0] = -random.randrange(120, 240) / 60
         
        
# define event handlers
def new_game():
    global PADDLE1_POS, PADDLE2_POS, PADDLE1_VEL, PADDLE2_VEL
    global SCORE_ONE, SCORE_TWO
               
    BALL_POS = [WIDTH / 2 , HEIGHT / 2]
    SCORE_ONE = 0
    SCORE_TWO = 0
    PADDLE1_POS = HEIGHT / 2
    PADDLE2_POS = HEIGHT / 2
    PADDLE1_VEL = 0
    PADDLE2_VEL = 0
    RIGHT = True
    spawn_ball(random.choice([True, False]))

def draw(c):
    global SCORE_ONE, SCORE_TWO, PADDLE1_POS, PADDLE2_POS, BALL_POS, BALL_VEL       
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
 
    #FIX positions and layer(under) score
    c.draw_text(str(SCORE_ONE), (120, 200), 80, "grey", "sans-serif")
    c.draw_text(str(SCORE_TWO), (420, 200), 80, "grey", "sans-serif")         

    #Ball - positioning
    BALL_POS[0] += BALL_VEL[0]
    BALL_POS[1] += BALL_VEL[1]    
    
    #Ball - top and bottom bounds    
    if BALL_POS[1] < BALL_RADIUS:
        BALL_VEL[1] = -BALL_VEL[1]
    if BALL_POS[1] > HEIGHT - BALL_RADIUS:
        BALL_VEL[1] = -BALL_VEL[1]

    #Ball - Hit gutter or paddle / add point      
    if BALL_POS[0] - BALL_RADIUS < PAD_WIDTH:
        if BALL_POS[1] < PADDLE2_POS - PAD_HEIGHT or BALL_POS[1] > PADDLE2_POS + HALF_PAD_HEIGHT:
            spawn_ball(RIGHT)
            SCORE_TWO += 1    
        else:
            BALL_VEL[0] = -BALL_VEL[0] * VEL_MULTIPLIER
            
    if  BALL_POS[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
        if BALL_POS[1] < (PADDLE1_POS - PAD_HEIGHT) or BALL_POS[1] > (PADDLE1_POS + HALF_PAD_HEIGHT):
            spawn_ball(LEFT)
            SCORE_ONE += 1
        else:
            BALL_VEL[0] = -BALL_VEL[0] * VEL_MULTIPLIER   
           
    # draw ball  
    ball = c.draw_circle(BALL_POS, BALL_RADIUS, 2, "White", "Green")
    
    # draw paddles - Forum adaption idea
    paddle1 = c.draw_line([HALF_PAD_WIDTH,PADDLE2_POS+HALF_PAD_HEIGHT], [HALF_PAD_WIDTH,PADDLE2_POS-HALF_PAD_HEIGHT],8, "red")
    paddle2 = c.draw_line([WIDTH - HALF_PAD_WIDTH,PADDLE1_POS+HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH,PADDLE1_POS-HALF_PAD_HEIGHT],8, "blue")

    # Update paddle's vertical position, keep paddle on the screen

    PADDLE1_POS += PADDLE1_VEL
    PADDLE2_POS += PADDLE2_VEL
     
    # Keep paddles on the screen
    if PADDLE1_POS <= HALF_PAD_HEIGHT:
        PADDLE1_POS = HALF_PAD_HEIGHT
    if PADDLE2_POS <= HALF_PAD_HEIGHT:
        PADDLE2_POS = HALF_PAD_HEIGHT
       
    if PADDLE1_POS >= HEIGHT - HALF_PAD_HEIGHT:
        PADDLE1_POS = HEIGHT - HALF_PAD_HEIGHT
    if PADDLE2_POS >= HEIGHT - HALF_PAD_HEIGHT:
        PADDLE2_POS = HEIGHT - HALF_PAD_HEIGHT
        
    
def keydown(key):
    global PADDLE1_VEL, PADDLE2_VEL

    if key == simplegui.KEY_MAP['up']:
        PADDLE1_VEL = -10
    elif key == simplegui.KEY_MAP['down']:
        PADDLE1_VEL = 10
    elif key == simplegui.KEY_MAP['w']:
        PADDLE2_VEL = -10
    elif key == simplegui.KEY_MAP['s']:
        PADDLE2_VEL = 10
   
def keyup(key):
    global PADDLE1_VEL, PADDLE2_VEL

    if key == simplegui.KEY_MAP['up']:
        PADDLE1_VEL = 0
    elif key == simplegui.KEY_MAP['down']:
        PADDLE1_VEL = 0
    elif key == simplegui.KEY_MAP['w']:
        PADDLE2_VEL = 0
    elif key == simplegui.KEY_MAP['s']:
        PADDLE2_VEL = 0
                               

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 150)

# start frame
new_game()
frame.start()