def is_armstrong_number(number):    
    digits = str(number)
    total_digits = len(digits)

    armstrong_number = 0
    for digit in digits:
        armstrong_number += int(digit) ** total_digits

    if number == armstrong_number:
        return True
    else:
        return False