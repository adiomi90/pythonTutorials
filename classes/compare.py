class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(sel, other):
        return self.x > other.x and self.y > other.y


point_1 = Point(1, 2)
point_2 = Point(1, 2)
print(point_1 == point_2)
