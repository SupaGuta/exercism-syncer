"""This function changes the data format of letters and their point values in the game."""

def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:    
    """Transform the legacy data.
 
    :param dict legacy_data: legacy data structure.
    :return dict: new data structure.
    """
    out = {}
    for points, letters in legacy_data.items():
        for letter in letters:
            out[letter.lower()] = points

    return out