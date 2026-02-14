COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]
COLOR_VALUE = {color: i for i, color in enumerate(COLORS)}

PREFIXES = (
    (1_000_000_000, "giga"),
    (1_000_000, "mega"),
    (1_000, "kilo"),
)

def label(colors):
    a, b, exp = (COLOR_VALUE[c] for c in colors[:3])
    ohms = (10 * a + b) * (10 ** exp)

    prefix = ""
    if ohms != 0:
        for factor, name in PREFIXES:
            if ohms % factor == 0:
                ohms /= factor
                prefix = name
                break

    return f'{int(ohms)} {prefix}ohms'
