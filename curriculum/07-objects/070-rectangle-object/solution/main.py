class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("边长不能为负")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
