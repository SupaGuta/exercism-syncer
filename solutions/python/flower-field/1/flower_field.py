def annotate(garden):
    # Empty board is valid
    if not garden:
        return []

    height = len(garden)
    width = len(garden[0])

    # Validate rectangular shape
    if any(len(row) != width for row in garden):
        raise ValueError("The board is invalid with current input.")

    # Validate allowed characters
    if any(ch not in "* " for row in garden for ch in row):
        raise ValueError("The board is invalid with current input.")

    annotaded_garden = []
    for row in range(height):
        new_row = []
        for col in range(width):
            if garden[row][col] == "*":
                new_row.append("*")
                continue

            count = 0
            for diff_row in (-1, 0, 1):
                for diff_col in (-1, 0, 1):
                    # Don't check current position
                    if diff_row == 0 and diff_col == 0:
                        continue

                    # Check positions around
                    check_row, check_col = row + diff_row, col + diff_col
                    if 0 <= check_row < height and 0 <= check_col < width and garden[check_row][check_col] == "*":
                        count += 1

            new_row.append(str(count) if count else " ")

        annotaded_garden.append("".join(new_row))
            
    return annotaded_garden
            

    
