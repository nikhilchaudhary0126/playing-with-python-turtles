"""
file: spinPattern.py
description:
creates spins using square designs

language: python3
"""

import turtle

# window dimensions
WINDOW_LENGTH = 800
SIDE_LENGTH = 400


def spin(match):
    """
    Call spin recursively
    """
    turtle.fd(match)
    turtle.rt(90)
    spin(match-10)


def main():
    """
    The main function
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Spin")

    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-SIDE_LENGTH/2, -SIDE_LENGTH/2)
    turtle.pendown()
    turtle.left(90)
    turtle.color('green')
    turtle.pensize(2)
    spin(SIDE_LENGTH)
    turtle.mainloop()


if __name__ == '__main__':
    main()
