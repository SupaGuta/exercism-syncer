def is_isogram(string):
    string = string.translate({ord('-'): None, ord(' '): None}).lower()
    return bool(len(string) == len(set(string)))