def egg_count(display_value):
    
    if display_value == 0: return 0

    binary_digits = []
    while display_value > 0:
        binary_digits.insert(0, display_value % 2)
        display_value //= 2

    return sum(binary_digits)
