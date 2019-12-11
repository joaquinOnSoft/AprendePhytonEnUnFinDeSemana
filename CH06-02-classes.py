# Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return str(self.x) + "," + str(self.y)

    def sum(self, point):
        return Point(self.x + point.x, self.y + point.y)

# Triangle class
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def toString(self):
        return "p1: " +self.p1.toString() + " p2: " + self.p2.toString() + " p3: " + self.p3.toString()

# MAIN
p1 = Point(5, 5)
p2 = Point(3, 6)
p3 = Point(0, 0)

print("Point 1: ", p1.toString())
print("Point 2: ", p2.toString())
print("Point 1 + 2: ", (p1.sum(p2)).toString())
triangle = Triangle(p1, p2, p3)
print(triangle.toString())

