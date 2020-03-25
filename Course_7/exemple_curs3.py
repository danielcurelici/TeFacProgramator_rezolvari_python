class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
        
    def __str__(self):
        return "Vector2D(%i, %i)" % (self.x, self.y)
        
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
        
if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(5, 1)
    v3 = v1 + v2
    print(v3.x, v3.y)
    print(v3)
    print(v3 - v1)