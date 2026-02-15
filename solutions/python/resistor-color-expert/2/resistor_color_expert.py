DIGITS = {
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

TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}

PREFIXES = (
    (1_000_000_000, "giga"),
    (1_000_000, "mega"),
    (1_000, "kilo"),
)

def resistor_label(colors):
    tot_colors = len(colors)

    if (tot_colors == 1): return "0 ohms"
    
    tot_digits = tot_colors - 2
    digits = [DIGITS[c] for c in colors[:tot_digits]]
    multiplier = 10 ** DIGITS[colors[-2]]
    ohms = int("".join(map(str, digits))) * multiplier
    
    prefix = ""
    for factor, name in PREFIXES:
        if ohms >= factor:
            ohms /= factor
            prefix = name
            break 

    tolerance = f" ±{TOLERANCES[colors[-1]]}%"

    return f'{ohms:g} {prefix}ohms{tolerance}'
