import math

################
### Constant ###
################

TOLERANCE = 1e-5

###############
### Classes ###
###############

class Point:
    def __init__(self, x: float, y: float, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def get_dim(self):
        if self.z == 0:
            return 2
        return 3

    def __add__(self, point: "Point"):
        res_x = self.x + point.x
        res_y = self.y + point.y
        res_z = self.z + point.z
        return Point(x=res_x, y=res_y, z=res_z)

    def __sub__(self, point: "Point"):
        res_x = self.x - point.x
        res_y = self.y - point.y
        res_z = self.z - point.z
        return Point(x=res_x, y=res_y, z=res_z)

class Vector:
    def __init__(self, x: float, y: float, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def get_dim(self):
        if self.z == 0:
            return 2
        return 3

    def get_norm(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def get_normalized_vector(self):
        norm = self.get_norm()
        x = self.x / norm
        y = self.y / norm
        z = self.z / norm
        return Vector(x, y, z)

    def normalize(self):
        self = self.get_normalized_vector()

    def __add__(self, vector: "Vector"):
        res_x = self.x + vector.x
        res_y = self.y + vector.y
        res_z = self.z + vector.z
        return Vector(x=res_x,
                      y=res_y,
                      z=res_z)

    def __sub__(self, vector: "Vector"):
        res_x = self.x - vector.x
        res_y = self.y - vector.y
        res_z = self.z - vector.z
        return Vector(x=res_x,
                      y=res_y,
                      z=res_z)

    def __mul__(self, arg: "Vector" | float):
        if isinstance(arg, Vector):
            return self.x * arg.x + self.y * arg.y + self.z * arg.z
        elif isinstance(arg, float):
            return Vector(x=arg * self.x,
                          y=arg * self.y,
                          z=arg * self.z)
        else:
            raise ValueError

    def __xor__(self, vector: "Vector"):
        pass

class Line:
    def __init__(self, point: Point, vector: Vector):
        self.origin_point = point
        self.direction = vector.get_normalized_vector()

class Plane:
    def __init__(self, point: Point, normal: Vector):
        self.normal = normal
        self.origin_point = point

#################
### Functions ###
#################

### Creation ###

def create_line_point_point(point_1: Point, point_2: Point):
    vector = convert_point_to_vector(point_2 - point_1).get_normalized_vector()
    return Line(point=point_1,
                vector=vector)


### Conversion ###

def convert_point_to_vector(point: Point):
    return Vector(x=point.x,
                  y=point.y,
                  z=point.z)

### Operations ###
