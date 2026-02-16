def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word_lower = word.lower()
    word_length = len(word)
    sorted_word = sorted(word_lower)

    valid_candidates = []
    for w in candidates:
        if len(w) != word_length: continue
        w_l = w.lower()
        if w_l == word_lower: continue
        if sorted(w_l) == sorted_word: valid_candidates.append(w)

    return valid_candidates