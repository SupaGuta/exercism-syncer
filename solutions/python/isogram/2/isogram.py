def is_isogram(string):
    string = [i for i in string.lower() if i.isalpha()]
    return len(string) == len(set(string))