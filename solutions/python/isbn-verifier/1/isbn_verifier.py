def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10: return False
    
    if not (isbn[:9].isdigit() and (isbn[-1].isdigit() or isbn[-1] in "Xx")): return False

    total = sum(
        (i + 1) * (10 if (i == 0 and ch in "Xx") else int(ch))
        for i, ch in enumerate(isbn[::-1])
    )
    return total % 11 == 0
