def is_triangle(fn):
    def wrapper(sides):
        return sum(sides) > 2 * max(sides) and min(sides) > 0 and fn(sides)    
    return wrapper

@is_triangle
def equilateral(sides):
    return sides[0] == sides[1] and sides[1] == sides[2]

@is_triangle
def isosceles(sides):
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]

@is_triangle
def scalene(sides):
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]

