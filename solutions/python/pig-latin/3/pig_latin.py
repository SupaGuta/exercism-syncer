VOWELS = ('a', 'e', 'i', 'o', 'u')
STARTS = ('xr', 'yt')
END = 'ay'

def translate(text: str):
    output = []
    for word in text.strip().lower().split():
        if word.startswith(VOWELS + STARTS):
            output.append(word + END)
            continue            
        
        for idx in range(1, len(word)):
            if word[idx] in set(VOWELS + ('y',)):
                idx += 1 if word[idx] == "u" and word[idx-1] == "q" else 0
                output.append(word[idx:] + word[:idx] + END)
                break

    return " ".join(output)