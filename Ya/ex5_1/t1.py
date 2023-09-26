class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    point = Point(3, 5)
    print(point.x, point.y)