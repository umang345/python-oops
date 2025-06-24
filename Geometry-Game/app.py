from point import Point
from rectangle import Rectangle
from random import randint 

x1 = randint(0,5)
x2 = randint(x1+1,10)
y1 = randint(0,5)
y2 = randint(y1+1,10)
p1 = Point(x1, y1)
p2 = Point(x2, y2)

rect = Rectangle(p1,p2)

print(f"Rectangle coordinates : {rect}")

# Get point and area from user
user_point = Point(
    float(input("Guess x : ")),
    float(input("Guess y : "))
)

user_area = float(input("Guess rectangle area : "))

# Print out game result
print(f"Your point was inside the rectangle : {rect.containsPoint(user_point)}")
print(f"Your area was off by: {rect.area() - user_area}")