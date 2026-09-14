from karel.stanfordkarel import *

"""
File: MoveAndDrop.py
----------------------
Karel starts in the bottom-left corner of the world facing east.
Karel moves forward two spaces and puts down one beeper on
Avenue 3.
"""


def main():
    """
    Moves Karel two spaces forward and places one beeper.
    """
    move()
    move()
    put_beeper()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()