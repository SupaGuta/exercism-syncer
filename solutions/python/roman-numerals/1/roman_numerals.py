NUMBERS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
)

def roman(number):
    out = []
    for value, symbol in NUMBERS:
        quotient, number = divmod(number, value)
        if quotient:
            out.append(symbol * quotient)

    return "".join(out)