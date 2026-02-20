"""Function to recite the lyrics to the Bottle Song."""

NUMBERS = ( "no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" )
TOP = "{num} green bottle{s} hanging on the wall,"
MIDDLE = "And if one green bottle should accidentally fall,"
BOTTOM = "There'll be {num} green bottle{s} hanging on the wall."

def recite(start: int, take: int = 1) -> list[str]:
    """Recite the Bottle Song.
 
    :param int start: starting verse number.
    :param int take: how many verses to include, defaults to 1.
    :return list[str]: the verses.
    """
    verses = []
    end = start - take
    for verse in range(start, start - take, -1):
        verses.extend([TOP.format(num = NUMBERS[verse].capitalize(), s = "s" if verse != 1 else "")] * 2)
        verses.append(MIDDLE)
        verses.append(BOTTOM.format(num = NUMBERS[verse - 1], s = "s" if verse - 1 != 1 else ""))
        if verse > end + 1: verses.append("")       

    return verses