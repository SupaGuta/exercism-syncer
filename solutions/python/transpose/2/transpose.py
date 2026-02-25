"""Transpose"""
from itertools import zip_longest

def transpose(text):
    """Given an input text output it transposed.

    :param text: string - the text to be transposed.
    :return: string - the transposed text.
    """
    rows = text.splitlines()

    out = []
    for col in zip_longest(*rows, fillvalue=None):
        last_char = max((idx for idx, char in enumerate(col) if char is not None)) 
        out.append("".join(" " if char is None else char for char in col[: last_char + 1]))
    
    return "\n".join(out)