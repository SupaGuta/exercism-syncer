COMMANDS = [
    lambda x: x.append("wink"),
    lambda x: x.append("double blink"),
    lambda x: x.append("close your eyes"),
    lambda x: x.append("jump"),
    lambda x: x.reverse()
]

def commands(binary_str: str) -> list[str]:
    handshake = []
    for idx, bit in enumerate(binary_str[::-1]):
        if bit == "1":
            COMMANDS[idx](handshake)
    return handshake