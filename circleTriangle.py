__author__ = 'nc'
"""
file: circleTriangle.py
description:
creates triangles and circles recursively

language: python3
"""

import turtle

# global constants for colors
COLORS = 'blueviolet', 'violet', 'blue', 'red', 'green', 'orange'

# global constants for window dimensions and side length
WINDOW_LENGTH = 800
SIDE_LENGTH = 300


def draw_triangles_rec(length, depth):
    """
    Draws triangles and  circles recursively

    :pre: (relative)pos (0,0), heading(east), pen down
    :post: (relative)pos (0,0), heading(east), pen down
    :param: length  length of triangle side
    :return: sum of diameters of circle = length/2
    """
    sum = 0
    if depth == 0:
        return 0
    elif depth == 1:
        turtle.pencolor(COLORS[depth % len(COLORS)])
        turtle.pendown()
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
        turtle.forward(length / 2)
        turtle.circle(length / 4)
        turtle.backward(length / 2)
        return length / 2
    else:
        turtle.pendown()
        turtle.pencolor(COLORS[depth % len(COLORS)])
        turtle.forward(length)
        turtle.left(120)
        for _ in range(2):
            turtle.forward(length / 2)
            turtle.right(120)
            sum += draw_triangles_rec(length / 2, depth - 1)
            turtle.pencolor(COLORS[depth % len(COLORS)])
            turtle.left(120)
            turtle.forward(length / 2)
            turtle.left(120)
        turtle.forward(length / 2)
        turtle.circle(length / 4)
        turtle.backward(length / 2)
        sum += length / 2
        return sum


def main():
    """
    The main function
    :pre: (relative)pos (0,0), heading(east), pen down
    :post: (relative)pos (0,0), heading(east), pen up
    :return: None-
    """
    # depth = int(input("Depth: "))
    depth = 5

    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)

    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Draw Star")
    turtle.speed(0)
    turtle.penup()
    turtle.showturtle()
    turtle.backward(SIDE_LENGTH/2)

    # write program name
    turtle.forward(SIDE_LENGTH / 2)
    turtle.right(90)
    turtle.color('white')
    turtle.forward(WINDOW_LENGTH / 2 - 50)
    turtle.write("TRIANGLES and CIRCLES", align='center', font=("Arial", 14, 'normal', 'bold'))
    turtle.back(WINDOW_LENGTH / 2 - 50)
    turtle.left(90)
    turtle.backward(SIDE_LENGTH / 2)

    turtle.pensize(2)
    print("Total diameter: ", int(draw_triangles_rec(SIDE_LENGTH, depth)))
    turtle.penup()
    turtle.update()
    turtle.mainloop()


if __name__ == '__main__':
    main()
