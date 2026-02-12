from math import isqrt

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    if number == 1:
        return "deficient"
    
    aliquot_sum = 1
    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            quotient = number // divisor
            aliquot_sum += divisor + (quotient if quotient != divisor else 0)
    
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
