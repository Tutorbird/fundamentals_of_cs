# Rock-paper-scissors-lizard-Spock template
# Nestor Alvarez, 2070115
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    return {
        'rock': 0,
        'Spock': 1,
        'paper': 2,
        'lizard': 3,
        'scissors': 4
    }.get(name, None)


def number_to_name(number):
    return {
        0: 'rock',
        1: 'Spock',
        2: 'paper',
        3: 'lizard',
        4: 'scissors'
    }.get(number, None)

def print_screen(player_choice, computer_choice):
    print "Player chooses", player_choice
    print "Computer chooses", computer_choice

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below

    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    computer_choice = number_to_name(comp_number)
    difference = comp_number - player_number % 5

    if difference > 2 :
        print_screen(player_choice, computer_choice)
        print "Computer wins!"
    elif difference == 0 :
        print_screen(player_choice, computer_choice)
        print "Player and computer tie!"
    else:
        print_screen(player_choice, computer_choice)
        print "Player wins!"

    print ""
    return None

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


    