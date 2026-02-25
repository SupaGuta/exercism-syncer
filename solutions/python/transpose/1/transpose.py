from itertools import zip_longest

def transpose(text):
    rows = text.splitlines()

    out = []
    for col in zip_longest(*rows, fillvalue=None):
        last_char = max((idx for idx, ch in enumerate(col) if ch is not None)) 
        out.append("".join(" " if ch is None else ch for ch in col[: last_char + 1]))
    
    return "\n".join(out)