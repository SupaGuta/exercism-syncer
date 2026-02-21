"""Word Count"""
import string

TRANS = str.maketrans({",": " ", "_": " "})
PUNCT = string.punctuation

def count_words(sentence: str) -> dict[str, int]:
    """Function to count how many times each word occurs in a given text
    
    :param sentence: str - Text to count words from.
    :return: dict[str, int] - The words counted."""

    counter: dict[str, int] = {}

    for token in sentence.lower().translate(TRANS).split():
        word = token.strip(PUNCT)
        if not word:
            continue
        counter[word] = counter.get(word, 0) + 1

    return counter