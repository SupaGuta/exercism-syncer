def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:
        number = number / 2 if not number % 2 else number * 3 + 1
        steps += 1

    return steps