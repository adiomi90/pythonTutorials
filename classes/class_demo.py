class Point:
    
    
    def __init__ (self, x, y):
        self.x = x 
        self.y = y 
        
    @classmethod
    def zero(cls):
        return cls(0, 0)
    
    def draw(self):
        print("draw")
point = Point.zero()
point.draw()

print(type(point))
print(isinstance(point, Point))

# class is a blueprint for creating object
# object is the instance of the class