from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, _x, _y):
        self.x += _x
        self.y += _y

    def length(self, p):
        return round(sqrt((self.x - p.x)**2 + (p.y - self.y)**2), 2)


if __name__ == '__main__':
    # point = Point(3, 5)
    # print(point.x, point.y)
    # point.move(2, -3)
    # print(point.x, point.y)
    first_point = Point(2, -7)
    second_point = Point(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))
