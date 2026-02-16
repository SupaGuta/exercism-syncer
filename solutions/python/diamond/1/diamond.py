from string import ascii_uppercase

def rows(letter: str) -> list[str]:
    letter = letter.upper()
    letter_index = ascii_uppercase.index(letter)

    diamond = []
    for idx in range(letter_index + 1):
        L = ascii_uppercase[idx]
        outer_spaces = letter_index - idx
        if idx == 0:
            line = " " * outer_spaces + L + " " * outer_spaces
        else:
            inner_spaces = 2 * idx - 1
            line = " " * outer_spaces + L + " " * inner_spaces + L + " " * outer_spaces
        diamond.append(line)

    return diamond + diamond[-2::-1]