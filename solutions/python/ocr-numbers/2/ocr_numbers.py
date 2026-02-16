NUMBERS = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}

W, H = 3, 4

def convert(input_grid: list[str]) -> str:

    # Validate row count
    height = len(input_grid)
    if not input_grid or height % H != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # Validate consistent column width
    width = len(input_grid[0])
    if any(len(row) != width for row in input_grid) or width % W:
        raise ValueError("Number of input columns is not a multiple of three")

    digits_per_row = width // W
    decoded_rows = []

    # Process in blocks of 4 rows
    for row in range(0, height, H):
        block = input_grid[row:row + H]

        decoded_glyphs = []
        # Process each digit column in that block
        for col in range(digits_per_row):
            start = col * W
            end = start + W
            glyph = tuple(row[start:end] for row in block)
            decoded_glyphs.append(NUMBERS.get(glyph, "?"))

        decoded_rows.append("".join(decoded_glyphs))

    return ",".join(decoded_rows)