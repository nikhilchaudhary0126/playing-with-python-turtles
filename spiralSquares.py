"""
file: spiralSquares.py
description:
creates spiral using squares

language: python3
"""

import turtle

# global constants for window dimensions
WINDOW_LENGTH = 800


def spiral(side):
    """
    Draws spiral using squares
    """
    turtle.pendown()
    for i in range(1, 200):
        turtle.forward(side)
        turtle.left(91)
        side = side + 5


def main():
    """
    The main function
    """
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Spin")

    turtle.speed(0)
    turtle.pensize(2)
    turtle.color('orange')
    spiral(20)
    turtle.mainloop()


if __name__ == '__main__':
    main()
