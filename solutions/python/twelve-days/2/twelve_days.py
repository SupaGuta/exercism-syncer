INTRO = "On the {ordinal} day of Christmas my true love gave to me: "

ORDINALS = (
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth",
)

GIFTS = (
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)

def recite(start_verse: int, end_verse: int) -> list[str]:
    verses = []
    for day in range(start_verse - 1, end_verse):
        middle = ", ".join(GIFTS[i] for i in range(day, 0, -1))
        last = ("and " if day > 0 else "") + GIFTS[0]
        gifts = f"{middle}, {last}" if middle else last
        verses.append(INTRO.format(ordinal=ORDINALS[day]) + gifts + ".")
    return verses
