def is_pangram(sentence):
    return len(set([char for char in sentence.lower() if char.isalpha()])) == 26
