class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return str(self.x) + "," + str(self.y)

    def sum(self, point):
        return Point(self.x + point.x, self.y + point.y)


# MAIN
p1 = Point(5, 5)
p2 = Point(3, 6)

print("Point 1: ", p1.toString())
print("Point 2: ", p2.toString())
print("Point 1 + 2: ", (p1.sum(p2)).toString())
