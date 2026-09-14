from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
Karel walks from its starting position to the newspaper,
picks it up, and returns to its original position.
"""


def main():
    move_to_newspaper()
    pick_beeper()
    return_home()


def move_to_newspaper():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def return_home():
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()