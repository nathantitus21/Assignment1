from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
Karel repairs all of the stone columns by filling any missing
beepers. Columns may have different heights and may already
contain some beepers.
"""


def main():
    """
    Repairs every column in the world.
    """
    while front_is_clear():
        repair_column()
        move_four_spaces()

    repair_column()


def repair_column():
    """
    Fills all missing beepers in one column and returns Karel
    to the bottom of the column facing east.
    """
    turn_left()

    fill_corner()

    while front_is_clear():
        move()
        fill_corner()

    turn_around()

    while front_is_clear():
        move()

    turn_left()


def fill_corner():
    """
    Places a beeper only if the current corner does not
    already contain one.
    """
    if no_beepers_present():
        put_beeper()


def move_four_spaces():
    """
    Moves Karel four avenues east to the next column.
    """
    move()
    move()
    move()
    move()


def turn_around():
    """
    Turns Karel 180 degrees.
    """
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()