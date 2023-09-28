class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def perimeter(self):
        x = abs(self.point1[0]-self.point2[0])
        y = abs(self.point1[1]-self.point2[1])
        return round(2*x+2*y, 2)

    def area(self):
        x = abs(self.point1[0]-self.point2[0])
        y = abs(self.point1[1]-self.point2[1])
        return round(x*y, 2)


if __name__ == '__main__':
    # rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    # print(rect.perimeter())

    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.area())
