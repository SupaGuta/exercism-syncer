VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
STARTS = ('xr', 'yt')
END = 'ay '

def translate(text: str):
    output = ''
    for word in text.strip().lower().split():
        if word.startswith(VOWELS + STARTS):
            if word.startswith("y") and word[1] != "t":
                output += word[1:] + word[:1] + END
                continue
            output += word + END
            continue            
        
        for idx, char in enumerate(word):
            if char in set(VOWELS):
                if char == "u" and word[idx-1] == "q":
                    slice_idx = idx+1
                else:
                    slice_idx = idx
                output += word[slice_idx:] + word[:slice_idx] + END
                break

    return output.rstrip()

print(translate("yellow"))