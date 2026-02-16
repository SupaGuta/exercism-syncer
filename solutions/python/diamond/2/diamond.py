def rows(letter: str) -> list[str]:
    letters = [chr(ch) for ch in range(ord('A'), ord(letter) + 1)]
    vertical_seq = letters[:-1] + letters[::-1]
    horizontal_seq = letters[::-1] + letters[1:]
    return [''.join(v if v == h else ' ' for h in horizontal_seq) for v in vertical_seq]

print(rows("E"))