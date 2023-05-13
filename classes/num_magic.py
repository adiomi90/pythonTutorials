class Point:
    def __init__(self, x , y):
        self.x = x 
        self.y = y 
    
    def __str__(self):
        return f"{self.x, self.y}"
    
    def __add__(self, other):
        return Point(self.x + other.x , self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x , self.y - other.y)
    
    def __mul__(self, other):
        return Point(self.x * other.x , self.y * other.y)
    
    def __truediv__(self,other):
        return Point(round(self.x / other.x,2), round(self.y + other.y,2))
    
    
point_1 = Point(5001,190)
point_2 = Point(49,31)
print(str(point_1 + point_2))
print(str(point_1 - point_2))
print(str(point_1 * point_2))
print(str(point_1 / point_2))

