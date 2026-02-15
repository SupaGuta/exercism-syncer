BRACKETS = {')': '(', ']': '[', '}': '{'}
OPENNINGS = set(BRACKETS.values())

def is_paired(input_string):
    brackets = []
    for ch in input_string:
        if ch in OPENNINGS:
            brackets.append(ch)
        elif ch in BRACKETS:
            # Check if we have an opening bracket and if it corresponds to the closing one found
            if not brackets or brackets.pop() != BRACKETS[ch]:
                return False

    return not brackets # brackets should be empty if all brackets are correct in string
