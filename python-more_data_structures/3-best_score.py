#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Function gets the largest value in a dictionary.
    Args:
        dictionary: A dictionary whose values are numbers.

    Returns:
        The largest value in the dictionary.
    """
    if not a_dictionary:
        return None
    val = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == val:
            return key
    return key
