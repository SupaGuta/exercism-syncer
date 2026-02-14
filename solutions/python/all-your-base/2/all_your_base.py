def rebase(input_base, digits, output_base):
    if input_base < 2: raise ValueError("input base must be >= 2")
    if output_base < 2: raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits): raise ValueError("all digits must satisfy 0 <= d < input base")

    input_number = sum(d * input_base**i for i, d in enumerate(digits[::-1]))

    if input_number == 0: return [0]

    output_digits = []
    while input_number > 0:
        output_digits.insert(0, input_number % output_base)
        input_number //= output_base
        
    return output_digits