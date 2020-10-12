__author__ = 'nc'
"""
file: fractalTree.py
description:
creates a fractal tree

language: python3
"""

import turtle

# global constants for window, side and branch dimensions
BRANCH_DEPTH = 10
BRANCH_ANGLE = 15
WINDOW_LENGTH = 800
SIDE_LENGTH = 100
RATIO = 0.8


def drawRecTree(segments, size):
    """
    draws fractal tree by recursions
    :pre: (relative)pos , heading(north), pen down
    :post: (relative)pos , heading(north), pen down
    :return: None
    """
    length = 0
    if segments == 0:
        return 0
    else:
        turtle.pencolor('green')
        turtle.forward(size)
        turtle.left(BRANCH_ANGLE)
        length += drawRecTree(segments - 1, size * RATIO)
        turtle.right(BRANCH_ANGLE)
        turtle.right(BRANCH_ANGLE)
        length += drawRecTree(segments - 1, size * RATIO)
        turtle.left(BRANCH_ANGLE)
        length += size
        turtle.backward(size)
        return length


def init():
    """
    Set world coordinates and call drawRecTree,
    prints the total length of tree branches
-
    :pre: (relative)pos (0,0), heading(east), pen down
    :post: (relative)pos (0,0), heading(east), pen up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)

    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Draw Fractal Tree")
    turtle.penup()
    turtle.showturtle()

    # write program name
    turtle.right(90)
    turtle.color('white')
    turtle.forward(WINDOW_LENGTH / 2 - 50)
    turtle.write("Fractal Tree", align='center', font=("Arial", 14, 'normal', 'bold'))
    turtle.back(100)
    turtle.left(180)

    turtle.pensize(4)
    turtle.tracer(0, 0)
    turtle.forward(100)
    turtle.down()
    print("Total length of branches =", drawRecTree(BRANCH_DEPTH, SIDE_LENGTH))
    turtle.penup()
    turtle.update()
    turtle.mainloop()


def main():
    """
    The main function
    """
    init()


if __name__ == '__main__':
    main()
