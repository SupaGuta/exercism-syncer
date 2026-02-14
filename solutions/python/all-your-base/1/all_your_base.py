def rebase(input_base, digits, output_base):
    if input_base < 2: raise ValueError("input base must be >= 2")
    if output_base < 2: raise ValueError("output base must be >= 2")

    input_number = 0
    for d in digits:
        if d < 0 or d >= input_base: raise ValueError("all digits must satisfy 0 <= d < input base")
        input_number = input_number * input_base + d

    if input_number == 0: return [0]

    output_digits = []
    while input_number > 0:
        output_digits.append(input_number % output_base)
        input_number //= output_base

    output_digits.reverse()
    return output_digits