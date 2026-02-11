def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    a, b, c = sides
    return is_triangle(a, b, c) and a == b and b == c


def isosceles(sides):
    a, b, c = sides
    return is_triangle(a, b, c) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides
    return is_triangle(a, b, c) and a != b and b != c and a != c

