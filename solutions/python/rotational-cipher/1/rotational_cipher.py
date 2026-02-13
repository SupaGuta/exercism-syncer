PLAIN = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    cipher = PLAIN[key:] + PLAIN[:key]
    return text.translate(str.maketrans(PLAIN + PLAIN.upper(), cipher + cipher.upper()))