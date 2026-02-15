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

TOLERANCE = {
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
    prefix = ""
    tolerance = ""
    tot_colors = len(colors)
    if (tot_colors == 1): return "0 ohms"
    
    tot_digits = tot_colors - 2
    digits = [COLORS[c] for c in colors[:tot_digits]]
    multiplier = 10 ** COLORS[colors[-2]]
    value_ohms = int("".join(map(str, digits))) * multiplier
    
    display_ohms = value_ohms
    for factor, name in PREFIXES:
        if value_ohms >= factor:
            value_ohms /= factor
            display_ohms = int(value_ohms) if value_ohms.is_integer() else value_ohms
            prefix = name
            break 

    tolerance = f" ±{TOLERANCE[colors[-1]]}%"

    return f'{display_ohms} {prefix}ohms{tolerance}'
