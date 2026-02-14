import re

def is_valid(isbn):
    isbn = str(isbn or "").replace("-", "")

    if not re.match(r'^\d{9}[\dX]$', isbn): return False 
    
    digits = [10 if d == 'X' else int(d) for d in isbn]    
    total = sum(d * (10 - i) for i, d in enumerate(digits))
    return total % 11 == 0
