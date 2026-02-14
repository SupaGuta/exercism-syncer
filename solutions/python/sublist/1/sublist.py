"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0

def contains(haystack, needle):
    """Return True if `needle` appears contiguously inside `haystack`."""
    if not needle: return True
    n = len(needle)
    return any(haystack[i:i+n] == needle for i in range(len(haystack) - n + 1))

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if contains(list_two, list_one):
        return SUBLIST
    if contains(list_one, list_two):
        return SUPERLIST
    return UNEQUAL
