from string import ascii_lowercase

ENCODING = {chr: ascii_lowercase[id] for id, chr in enumerate(ascii_lowercase[::-1])}

def encode(text: str, decode: bool = False) -> str:
    out = "".join(ENCODING.get(char, char) for char in text.lower() if char.isalnum())
    return out if decode else " ".join(out[index:index+5] for index in range(0, len(out), 5))

def decode(text: str) -> str:
    return encode(text, True)