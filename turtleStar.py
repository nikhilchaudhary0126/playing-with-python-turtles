__author__ = 'nc'
"""
file: turtleStar.py
description:
creates turtle star using while loop

language: python3
"""

import turtle

# global constants for window dimensions and side length
WINDOW_LENGTH = 800
SIDE_LENGTH = 300


def star(n):
    """
    draws start using turtle

    :pre: (relative)pos (0,0), heading(east), pen up
    :post: (relative)pos (0,0), heading(east), pen down
    :return: None
    """
    turtle.pendown()
    turtle.pensize(3)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(SIDE_LENGTH)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()


def draw():
    """
    The main function
    :pre: (relative)pos (0,0), heading(east), pen down
    :post: (relative)pos (0,0), heading(east), pen up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)

    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Draw Star")
    turtle.speed(9)
    turtle.penup()
    turtle.showturtle()

    # write program name
    turtle.forward(SIDE_LENGTH / 2)
    turtle.right(90)
    turtle.color('white')
    turtle.forward(WINDOW_LENGTH / 2 - 50)
    turtle.write("TURTLE  STAR", align='center', font=("Arial", 14, 'normal', 'bold'))
    turtle.back(WINDOW_LENGTH / 2 - 50)
    turtle.left(90)
    turtle.backward(SIDE_LENGTH / 2)

    # draw star
    star(3)
    turtle.mainloop()


def main():
    """
    The main function
    """
    print(__author__)
    draw()


if __name__ == '__main__':
    main()
