def score(x, y):
    # Dict (radius, points)
    circles = {
        10: 1,
        5: 5,
        1: 10
    }
    # Must be sorted by ascending radius
    circles_sorted = dict(sorted(circles.items()))
    print(circles_sorted)

    # Check points depending on dart position and radius
    dart_pos = x**2 + y**2
    score = 0
    for radius, points in circles_sorted.items():
        if dart_pos <= radius**2:
            score = points
            break
    
    return score