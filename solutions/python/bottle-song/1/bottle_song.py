NUMBERS = ( "no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" )
TOP = "{num} green bottle{s} hanging on the wall,"
MIDDLE = "And if one green bottle should accidentally fall,"
BOTTOM = "There'll be {num} green bottle{s} hanging on the wall."

def recite(start, take=1):
    verses = []
    end = start - take
    for number in range(start, end, -1):
        verses.extend([TOP.format(num = NUMBERS[number].capitalize(), s = "s" if number != 1 else "")] * 2)
        verses.append(MIDDLE)
        verses.append(BOTTOM.format(num = NUMBERS[number - 1], s = "s" if number - 1 != 1 else ""))
        if take != 1:
            verses.append("") 
            take -= 1

    return verses