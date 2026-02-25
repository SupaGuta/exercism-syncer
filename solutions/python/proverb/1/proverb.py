LINE = "For want of a {} the {} was lost."
END  = "And all for the want of a {}{}."

def proverb(*words, qualifier=None):
    if not words:
        return []

    lines = [LINE.format(word_1, word_2) for word_1, word_2 in zip(words, words[1:])]

    qualif = f"{qualifier} " if qualifier else ""
    lines.append(END.format(qualif, words[0]))

    return lines
