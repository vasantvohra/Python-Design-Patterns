class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementation-specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class Circle(object):
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of by another class: DrawingAPI"""
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def scale(self, percent):
        """Implementation-independent"""
        self.radius *= percent

if __name__ == '__main__':
    # Build the first Circle object using API One
    circle1 = Circle(1, 2, 3, DrawingAPIOne())
    # Draw a circle
    circle1.draw()

    # Build the second Circle object using API Two
    circle2 = Circle(2, 3, 4, DrawingAPITwo())
    # Draw a circle
    circle2.draw()