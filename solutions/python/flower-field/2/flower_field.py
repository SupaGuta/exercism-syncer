ADJACENT = [
    (dx, dy)
    for dx in (-1, 0, 1)
    for dy in (-1, 0, 1)
    if dx != 0 or dy != 0
]

def annotate(garden: list[str]) -> list[str]:
    height = len(garden)
    width = len(garden[0]) if garden else 0

    # rectangular check
    if not all(len(row) == width for row in garden):
        raise ValueError("The board is invalid with current input.")

    flowers: set[tuple[int, int]] = set()

    # collect flowers + validate chars
    for y, line in enumerate(garden):
        for x, val in enumerate(line):
            if val == "*":
                flowers.add((x, y))
            elif val != " ":
                raise ValueError("The board is invalid with current input.")

    def cell_value(x: int, y: int) -> str:
        if (x, y) in flowers:
            return "*"

        count = sum(((x + dx, y + dy) in flowers) for dx, dy in ADJACENT)
        return str(count) if count else " "

    return [
        "".join(cell_value(x, y) for x in range(width))
        for y in range(height)
    ]
