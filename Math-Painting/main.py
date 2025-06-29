from canvas import Canvas
from shapes import Square, Rectangle

canvas = Canvas(height=20, width=30,color=(255,255,255))
r1 = Rectangle(1,6,10,7,(100,200,125))
r1.draw(canvas)
s1 = Square(1,3,3,(0,100,200))
s1.draw(canvas)
canvas.make("export/canvas.png")