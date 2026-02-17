DAYS = (
    ("first", "a Partridge"),
    ("second", "two Turtle Doves"),
    ("third", "three French Hens"),
    ("fourth", "four Calling Birds"),
    ("fifth", "five Gold Rings",),
    ("sixth", "six Geese-a-Laying"),
    ("seventh", "seven Swans-a-Swimming"),
    ("eighth", "eight Maids-a-Milking"),
    ("ninth", "nine Ladies Dancing"),
    ("tenth", "ten Lords-a-Leaping"),
    ("eleventh", "eleven Pipers Piping"),
    ("twelfth", "twelve Drummers Drumming")
)

def recite(start_verse, end_verse):
    out = []
    for day in range(start_verse - 1, end_verse):

        verse = []        
        verse.append(f"On the {DAYS[day][0]} day of Christmas my true love gave to me: ")
        for v in range(day, -1, -1):
            if v == 0 and day > 0:
                verse.append("and ")
                
            verse.append(f"{DAYS[v][1]}")

            if v != 0:
                verse.append(", ")
            else:
                verse.append(" in a Pear Tree.")

        out.append("".join(verse))

    return out

print(recite(2, 2))