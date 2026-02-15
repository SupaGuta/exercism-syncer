def square_root(number):
    guess = max(1, number // 2)
    while guess * guess != number:
        guess = (number // guess + guess) // 2

    return guess
