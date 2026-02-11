def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    next_number = number
    while next_number != 1:
        if next_number % 2 == 0:
            next_number /= 2
        else:
            next_number = next_number * 3 + 1

        steps += 1

    return steps
