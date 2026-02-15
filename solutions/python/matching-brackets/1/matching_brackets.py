CLOSING = {')': '(', ']': '[', '}': '{'}
OPENING = set(CLOSING.values())

def is_paired(input_string):
    brackets = []
    for ch in input_string:
        if ch in OPENING:
            brackets.append(ch)
        elif ch in CLOSING:
            # Check if we have an opening bracket and if it corresponds to the closing one found
            if not brackets or brackets[-1] != CLOSING[ch]:
                return False
            # If bracket correspons to closing then remove opening bracket
            brackets.pop()

    return not brackets # brackets should be empty if all brackets are correct in string
