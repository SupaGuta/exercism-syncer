def find(search_list: list[str], value: int) -> int:
    sorted_list = sorted((val, idx) for idx, val in enumerate(search_list))

    while sorted_list:
        mid_idx = len(sorted_list) // 2
        mid_val, orig_idx = sorted_list[mid_idx]
        
        if mid_val > value:
            sorted_list = sorted_list[:mid_idx]
        elif mid_val < value:
            sorted_list = sorted_list[mid_idx + 1:]
        else:
            return orig_idx

    raise ValueError("value not in array")   