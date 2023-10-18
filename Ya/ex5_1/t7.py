class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_pos(self):
        if self.point1[0] <= self.point2[0]:
            return (self.point1[0], self.point2[1])
        else:
            return (self.point2[0], self.point2[1])

    def get_size(self):
        x = abs(self.point1[0] - self.point2[0])
        y = abs(self.point1[1] - self.point2[1])
        return (round(x, 2), round(y, 2))

    def move(self, _x, _y):
        self.point1 = (round(self.point1[0] + _x, 2),
                       round(self.point1[1] + _y, 2))
        self.point2 = (round(self.point2[0] + _x, 2),
                       round(self.point2[1] + _y, 2))

    def resize(self, _x, _y):
        if self.point1[0] > self.point2[0]:
            self.point1 = (self.point2[0] , self.point2[1])
            self.point2 = (self.point2[0] + _x, self.point2[1] + _y)
        else:
            self.point2 = (round(self.point2[0] + _x, 2),
                           round(self.point2[1] + _y, 2))


if __name__ == '__main__':
    # rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    # print(rect.get_pos()   , rect.get_size())
    # rect.move(1.32, -5)
    # print(rect.get_pos(), rect.get_size())
    # (3.2, 3.14) (4.32, 7.44)
    # (4.52, -1.86) (4.32, 7.44)

    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.resize(23.5, 11.3)
    print(rect.get_pos(), rect.get_size())
    # (3.2, 3.14) (4.32, 7.44)
    # (3.2, 3.14) (23.5, 11.3)
