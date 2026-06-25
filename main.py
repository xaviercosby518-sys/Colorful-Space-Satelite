# Importing the libraries to create the satelite
import turtle
# Creating the canvas
turtle.Screen().setup(560,560)
import grid

# set the color of the satelite
turtle.fillcolor("rgba(221, 29, 29, 0.5)")
# begin the color fill
turtle.begin_fill()
# Create a square shaped satelite body
turtle.forward(-80)
turtle.speed(5)
turtle.left(-90)
turtle.forward(-80)
turtle.left(-90)
turtle.forward(-80)
turtle.left(-90)
turtle.forward(-80)
turtle.end_fill()

turtle.fillcolor("rgba(0, 103, 255, 0.5)")
turtle.begin_fill()

# Creating the triangle reflector
turtle.forward(80)
turtle.left(26.2)
turtle.forward(90)
turtle.left(-52.5)
turtle.forward(-90)
turtle.end_fill()

turtle.fillcolor("rgba(103, 255, 104, 0.5)")
turtle.begin_fill()

# Creating the left solar panel
turtle.left(116)
turtle.forward(80)
turtle.left(90)
turtle.forward(80)
turtle.left(90.2)
turtle.forward(80)
turtle.end_fill()

turtle.fillcolor("rgba(218, 0, 255, 0.5)")
# cool purple - rgba(159, 0, 255, 0.53)
turtle.begin_fill()

# Creating the right solar panel
turtle.forward(160)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(85)
turtle.end_fill()