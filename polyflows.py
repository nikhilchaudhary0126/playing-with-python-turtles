__author__ = 'nc'
"""
file: polyflows.py
description:
creates polyflows and polygons using recursion

language: python3
"""


import turtle

# "constants" for the color used at each depth, e.g. depth=1 is 'red'
COLORS = 'blueviolet', 'violet', 'blue', 'red', 'yellow', 'green', 'orange'

# window dimensions
WINDOW_LENGTH = 800
SIDE_LENGTH = 100


def init():
    """
    This function will set up the window, coordinate system
    and draw the program names

    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading north, pen up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Polygon Pattern")
    turtle.color('white')
    turtle.penup()
    turtle.right(90)
    turtle.forward(WINDOW_LENGTH / 2 - 50)
    turtle.write("Polyflows and Ploygons", align='center', font=("Arial", 14, 'normal', 'bold'))
    turtle.back(WINDOW_LENGTH / 2 - 50)
    turtle.left(90)
    turtle.tracer(0, 0)


def polygon(numsides, size, drawfillunfill, sumside):
    """
    Draw a regular polygon of given number of sides

    :param: numsides    number of sides of polygon
    :param: size    length of side of polygon
    :param: drawfillunfill  fill and unfill polygons based on command line in main
    :param: sumside     sum of previous recursive sides of polygons
    :pre: pos (0,0), heading (east), pen up
    :post: pos (0,0), heading (east), pen down
    :return: sumside    sum of all recursive sides of polygons
    """
    turtle.pendown()
    turtle.color(COLORS[numsides % len(COLORS)])  # draw the circle with the defined line colo
    if numsides < 3:
        pass
    else:

        # fill polygons recursively
        if drawfillunfill == 'fill':
            turtle.fillcolor(COLORS[numsides % len(COLORS)])  # fill the circle
            turtle.begin_fill()
            for _ in range(numsides):
                turtle.left(360 / numsides)
                turtle.forward(size)
            turtle.end_fill()

        # draw polygon shapes recursively
        for _ in range(numsides):
            turtle.left(360 / numsides)
            turtle.forward(size)
            sumside = size + polygon(numsides - 1, size / 2, drawfillunfill, sumside)

    return sumside


def main():
    """
    The main function to handle command line arguments and
    draw polygons of decreasing sides, recursively.

    :pre: pos (0,0), heading (east), pen down
    :post: pos (0,0), heading (east), pen down
    :return: None
    """
    side = 6
    fillunfill = "fill"
    totalsum = 0
    loopcount = side * 2

    # Draw design change for side = 8 as it has high recursive values
    if side == 8:
        loopcount = 4
        print("Please wait as recursion drawings may take time for high recursive images")

    # As stated sides should be between defined inputs
    if side < 3 or side > 8:
        raise ValueError

    init()
    for _ in range(loopcount):
        totalsum += polygon(side, SIDE_LENGTH, fillunfill, sumside=0)
        turtle.left(360 / loopcount)
    print("Sum of all sides: ", totalsum)
    turtle.update()
    turtle.mainloop()


if __name__ == '__main__':
    main()
