from point import Point

class Rectangle:
    def __init__(self,point1:Point, point2:Point):
        self.point1 = point1
        self.point2 = point2
    
    def containsPoint(self,point:Point):
        if ( self.point1.x < point.x  and point.x < self.point2.x ) \
        and ( self.point1.y < point.y  and point.y < self.point2.y ):
            return True 
    
        return False 

    def area(self):
        deltaX = abs(self.point1.x - self.point2.x)
        deltaY = abs(self.point1.y - self.point2.y)
        return deltaX * deltaY
    
    def __repr__(self) -> str:
        return f"{self.point1} and {self.point2}"
