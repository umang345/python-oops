from graphical_point import GraphicalPoint
from random import randint 
from graphical_rectangle import GraphicalRectangle
from point import Point

import turtle

x1 = randint(0,500)
x2 = randint(x1+1,800)
y1 = randint(0,500)
y2 = randint(y1+1,800)
p1 = Point(x1, y1)
p2 = Point(x2, y2)

rect = GraphicalRectangle(p1,p2)

print(f"Rectangle coordinates : {rect}")

# Get point and area from user
user_point = GraphicalPoint(
    float(input("Guess x : ")),
    float(input("Guess y : "))
)

myTurtle = turtle.Turtle()

rect.draw(canvas = myTurtle)
user_point.draw(canvas = myTurtle)

turtle.done()