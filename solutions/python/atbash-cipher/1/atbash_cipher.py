import string

PLAIN = "abcdefghijklmnopqrstuvwxyz"
CYPHER = "".join(sorted(PLAIN, reverse=True))
ENCODE = str.maketrans(PLAIN, CYPHER)
DECODE = str.maketrans(CYPHER, PLAIN)

def encode(plain_text):
    clean_text = "".join(ch for ch in plain_text.replace(" ", "").lower() if ch not in string.punctuation)
    encoded_text = clean_text.translate(ENCODE)
    return " ".join(encoded_text[iter:iter+5] for iter in range(0, len(encoded_text), 5))

def decode(ciphered_text):
    return ciphered_text.replace(" ", "").translate(DECODE)