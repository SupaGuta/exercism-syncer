COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

PREFIXES = (
    (1_000_000_000, "giga"),
    (1_000_000, "mega"),
    (1_000, "kilo"),
)

def label(colors):
    a, b, exp = (COLORS[c] for c in colors[:3])
    ohms = (10 * a + b) * (10 ** exp)

    prefix = ""
    if ohms != 0:
        for factor, name in PREFIXES:
            if ohms % factor == 0:
                ohms //= factor
                prefix = name
                break

    return f'{ohms} {prefix}ohms'
