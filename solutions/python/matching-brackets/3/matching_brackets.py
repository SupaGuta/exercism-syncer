BRACKETS = {')': '(', ']': '[', '}': '{'}
OPENNINGS = set(BRACKETS.values())

def is_paired(input_string):
    stack = []
    for ch in input_string:
        if ch in OPENNINGS:
            stack.append(ch)
        elif ch in BRACKETS:
            if not stack or stack.pop() != BRACKETS[ch]:
                return False

    return not stack
