def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word_c = word.casefold()
    sig = sorted(word_c)
    return [
        w for w in candidates
        if (w_c := w.casefold()) != word_c and sorted(w_c) == sig
    ]