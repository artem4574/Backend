import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other_point):
        return Point(self.x - other_point.x, self.y - other_point.y, self.z - other_point.z)

    def dot(self, other_point):
        return self.x * other_point.x + self.y * other_point.y + self.z * other_point.z

    def cross(self, other_point):
        return Point(
            self.y * other_point.z - self.z * other_point.y,
            self.z * other_point.x - self.x * other_point.z,
            self.x * other_point.y - self.y * other_point.x
        )

    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


def plane_angle(a, b, c, d):
    ab = b.__sub__(a)
    bc = c.__sub__(b)
    cd = d.__sub__(c)

    x = ab.cross(bc)
    y = bc.cross(cd)

    try:
        cos_phi = x.dot(y) / (x.absolute() * y.absolute())
    except ZeroDivisionError:
        print("Error: Zerodivision!")
        exit()
    angle_phi = math.degrees(math.acos(cos_phi))

    return angle_phi


if __name__ == '__main__':
    a = Point(10, 70, 6)
    b = Point(40, 50, 6)
    c = Point(25, 13, 9)
    d = Point(10, 11, 12)

    # print(plane_angle(a, b, c, d))
