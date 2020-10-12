"""
file: circles.py
description:
creates circle pattern

language: python3
"""

import turtle

# window dimensions and colors
WINDOW_LENGTH = 800
COLORS = 'green', 'cyan', 'blue', 'magenta', 'red', 'yellow'


def circles(n):
    """
    Draws circles
    :pre: pos(0,0), heading (east), pen pendown
    :post: pos(0,0), heading (east), pen pendown
    :return: None
    """
    for i in range(n):
        for col in range(6):
            turtle.color(COLORS[col % 6])
            turtle.circle(30 + i * 5)
            turtle.right(60)


def main():
    """
    The main function
    :pre: pos(0,0), heading (east), pen pendown
    :post: pos(0,0), heading (east), pen pendown
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Circles")

    turtle.speed(0)
    turtle.pensize(2)
    circles(35)
    turtle.mainloop()


if __name__ == '__main__':
    main()
