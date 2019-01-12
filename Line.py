import math

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        #Distance formula
        dist = ((x1-x2) ** 2 + (y1-y2)**2) ** 0.5
        print(dist)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        slo = (y2 - y1)/(x2 - x1)
        print(slo)

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
li.distance()
li.slope()

class Cylinder():
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = (math.pi) * self.height * (self.radius ** 2)
        print(vol)

    def surface_area(self):
        sa = 2 * (math.pi) * self.radius * (self.radius + self.height)
        print(sa)

c = Cylinder(2, 3)
c.volume()
c.surface_area()

