__author__ = 'nc'
"""
file: name.py
description:
This is a program that draws my name 'Nikhil'
Unique characters include N,I,K,H,L

language: python3
"""

import turtle
import math

# global constants for window dimensions
WINDOW_LENGTH = 800
# global constant for start coordinate on x axis
DRAW_START = 150
# global constants for character dimensions
CHAR_UNIT = 60
CHAR_SPACING = 30


def init():
    """
    Initialize the draw window
    :pre: pos(0,0), heading east, pen down
    :post: pos(DRAW_START,0), heading north, pen up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)
    turtle.hideturtle()
    turtle.up
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Name Generator")
    turtle.pensize(2)
    turtle.penup()

    # write program name
    turtle.right(90)
    turtle.forward(WINDOW_LENGTH / 2 - 50)
    turtle.color('white')
    turtle.write("Thanks to Python Turtle", align='center', font=("Arial", 20, 'normal', 'bold'))
    turtle.back(WINDOW_LENGTH / 2 - 50)
    turtle.left(90)

    turtle.speed(6)
    turtle.left(180)
    turtle.forward(DRAW_START)
    turtle.right(90)
    turtle.showturtle()


def drawName():
    """
    Draw all characters of name 'Nikhil'
    :pre: left corner at bottom(start of name), heading north, pen up
    :post: right corner at bottom(end of name), heading north, pen up
    :return: None
    """
    diagonal = math.sqrt(2 * (CHAR_UNIT ** 2))
    # start drawing
    drawN(diagonal)
    defaultSpace()
    drawI()
    defaultSpace()
    drawK(diagonal)
    defaultSpace()
    drawH()
    defaultSpace()
    drawI()
    defaultSpace()
    drawL()


def defaultSpace():
    """
    Creates a default space between characters
    :pre: left corner at bottom(start of default space), heading (north), pen up
    :post: right corner at bottom(end of default space), heading (north), pen up
    :return: None
    """
    turtle.right(90)
    turtle.forward(CHAR_SPACING)
    turtle.left(90)


def charSpace():
    """
    Creates a space of CHAR_UNIT size between names
    :pre: left corner at bottom(start of space), heading (north), pen up
    :post: right corner at bottom(end of space), heading (north), pen up
    :return: None
    """
    turtle.right(90)
    turtle.forward(CHAR_UNIT)
    turtle.left(90)


def drawN(diagonal):
    """
    Draws a character 'N'
    :pre: left corner at bottom(start of character N), heading (north), pen up
    :post: right corner at bottom(end of character N), heading (north), pen up
    :param: diagonal: diagonal length calculated in drawName
    :return: None
    """
    turtle.pendown()
    turtle.forward(CHAR_UNIT)
    turtle.right(135)
    turtle.forward(diagonal)
    turtle.left(135)
    turtle.forward(CHAR_UNIT)
    turtle.back(CHAR_UNIT)
    turtle.penup()


def drawI():
    """
    Draws a character 'I'
    :pre: left corner at bottom(start of character I), heading (north), pen up
    :post: right corner at bottom(end of character I), heading (north), pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward(CHAR_UNIT)
    turtle.backward(CHAR_UNIT)
    turtle.penup()


def drawK(diagonal):
    """
    Draws a character 'K'
    :pre: left corner at bottom(start of character K), heading (north), pen up
    :post: right corner at bottom(end of character K), heading (north), pen up
    :param: diagonal: diagonal length calculated in drawName
    :return: None
    """
    turtle.pendown()
    turtle.forward(CHAR_UNIT)
    turtle.right(180)
    turtle.forward(CHAR_UNIT / 2)
    turtle.left(135)
    turtle.forward(diagonal / 2)
    turtle.right(180)
    turtle.forward(diagonal / 2)
    turtle.left(90)
    turtle.forward(diagonal / 2)
    turtle.left(135)
    turtle.penup()


def drawH():
    """
    Draws a character 'H'
    :pre: left corner at bottom(start of character H), heading (north), pen up
    :post: right corner at bottom(end of character H), heading (north), pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward(CHAR_UNIT)
    turtle.backward(CHAR_UNIT / 2)
    turtle.right(90)
    turtle.forward(CHAR_UNIT)
    turtle.left(90)
    turtle.forward(CHAR_UNIT / 2)
    turtle.right(180)
    turtle.forward(CHAR_UNIT)
    turtle.left(180)
    turtle.penup()


def drawL():
    """
    Draws a character 'L'
    :pre: left corner at bottom(start of character L), heading (north), pen up
    :post: right corner at bottom(end of character L), heading (north), pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward(CHAR_UNIT)
    turtle.backward(CHAR_UNIT)
    turtle.right(90)
    turtle.forward(CHAR_UNIT / 2)
    turtle.left(90)
    turtle.penup()


def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), pen down
    :post: right corner at bottom(end of name), heading north, pen up
    :return: None
    """

    init()
    drawName()
    turtle.mainloop()


if __name__ == '__main__':
    main()
