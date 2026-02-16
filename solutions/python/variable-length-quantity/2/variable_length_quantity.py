CONT = 0x80
MASK7 = 0x7F
MAX32 = 0xFFFFFFFF

def encode(numbers: list[int]) -> list[int]:
    out: list[int] = []

    for n in numbers:      
        if n == 0:
            out.append(0)
            continue

        chunks = []
        while n > 0:
            chunks.append(n & MASK7)
            n >>= 7

        chunks.reverse()

        for i in range(len(chunks) - 1):
            chunks[i] |= CONT

        out.extend(chunks)

    return out


def decode(bytes_: list[int]) -> list[int]:  
      
    if bytes_[-1] & CONT:
        raise ValueError('incomplete sequence')
    
    out: list[int] = []
    value = 0

    for b in bytes_:
        value = (value << 7) | (b & MASK7)

        if not (b & CONT):
            out.append(value)
            value = 0

    return out
