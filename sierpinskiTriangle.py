__author__ = 'nc'
"""
file: turtleStar.py
description:
creates sierpinski triangle using while loop

language: python3
"""

import turtle

COLORS = 'blueviolet', 'violet', 'blue', 'red', 'green', 'orange'

WINDOW_LENGTH = 800
SIDE_LENGTH = 150


def draw_triangles_1(length):
    """
    Draw a red triangle
    :param length: Length of 1 side of triangle
    :pre: pos:lower left, turtle down , facing east
    :post: pos:lower left, turtle down , facing east
    :return: None
    """
    turtle.pencolor('red')
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)


def draw_triangles_2(length):
    """
    Draw a green triangle with red triangles at each vertex
    :param length: Length of 1 side of triangle
    :pre: pos:lower left of the triangle, turtle down , facing east
    :post: pos:lower left of the triangle, turtle down , facing east
    :return: None
    """
    turtle.pencolor('green')
    for _ in range(3):
        turtle.forward(length)
        draw_triangles_1(length / 2)
        turtle.pencolor('green')
        turtle.left(120)


def draw_triangles_rec(length, depth):
    """
    Draw a sierpinski triangle with different colored triangles
    :param length: Length of 1 side of triangle
    :param depth: Depth of recursion
    :pre: pos:lower left, turtle down , facing east
    :post: pos:lower left, turtle down , facing east
    :return: None
    """
    if depth == 0:
        pass
    elif depth == 1:
        turtle.pencolor(COLORS[depth % len(COLORS)])
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        turtle.pencolor(COLORS[depth % len(COLORS)])
        for _ in range(3):
            turtle.forward(length)
            draw_triangles_rec(length / 2, depth - 1)
            turtle.pencolor(COLORS[depth % len(COLORS)])
            turtle.left(120)


def main():
    """
    The main function to draw recursive triangles
    :pre: pos (0,0), heading (east), pen down
    :post: pos (0,0), heading (east), pen down
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Sierpinski Triangle")
    turtle.penup()

    # write program name
    turtle.right(90)
    turtle.forward(WINDOW_LENGTH / 2 - 50)
    turtle.color('white')
    turtle.write("Sierpinski Triangle", align='center', font=("Arial", 14, 'normal', 'bold'))
    turtle.back(WINDOW_LENGTH / 2 - 50)
    turtle.left(90)

    # initial shift for centering
    turtle.backward(SIDE_LENGTH / 2)
    turtle.pendown()

    # draw_triangles_2(SIDE_LENGTH)
    turtle.tracer(0, 0)
    turtle.pensize(2)
    draw_triangles_rec(SIDE_LENGTH, 6)
    turtle.mainloop()


if __name__ == '__main__':
    main()
