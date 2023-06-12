def equilateral(sides):
    if is_triangle(sides):
        a, b, c = sides
        if a == b == c:
            return True
        return False
    return False

  
def isosceles(sides):
    if is_triangle(sides):
        a, b, c = sides
        if a == b or b == c or a == c:
            return True
        return False
    return False


def scalene(sides):
    if is_triangle(sides):
        a, b, c = sides
        if a != b and b != c and a != c:
            return True
        return False
    return False


def is_triangle(sides):
    a, b, c = sides
    if not a or not b or not c:
        return False
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    return True
