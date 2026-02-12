# List of tuples (radius, points)
rules = [
    (10, 1),
    (1, 10),
    (5, 5)
]
# Must be sorted
rules = sorted(rules)

def score(x, y):
    # Return points depending on dart squared distance from radius
    dist2 = x**2 + y**2
    for radius, points in rules:
        if dist2 <= radius**2:
            return points
        
    return 0