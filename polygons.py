"""
file: polygons.py
description:
creates circle and ploygons around it

language: python3
"""

import turtle

# global constants for window dimensions and colors
WINDOW_LENGTH = 800
SIDE_LENGTH = 100
COLORS = 'red', 'orange', 'yellow'

def polygon(size, noofsides):
    """
    Creates a polygon

    :param size:    size of side of polygon
    :param noofsides:   polygons shape based on number of sides
    :return: 
    """
    for i in range(noofsides):
        turtle.forward(size)
        turtle.right(360/noofsides)
        #turtle.right(60)


def spiral(side):
    """
    Creates a circle and polygons around it

    :param side:
    :return:
    """
    turtle.pendown()
    turtle.left(180)
    for j in range(5):
        for i in range(1, 21):
            turtle.color('green')
            turtle.circle(side, 360 / 20)
            turtle.color(COLORS[i % 3])
            polygon(SIDE_LENGTH+j*50, 3)



def main():
    """
    The main function
    """
    # set turtle world
    turtle.setworldcoordinates(-WINDOW_LENGTH / 2, -WINDOW_LENGTH / 2,
                               WINDOW_LENGTH / 2, WINDOW_LENGTH / 2)
    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.title("Spiral")

    turtle.speed(0)
    turtle.pensize(2)
    spiral(20)
    turtle.mainloop()


if __name__ == '__main__':
    main()
