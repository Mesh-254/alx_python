#!/usr/bin/python3
def multiple_returns(sentence):
    """
        function that returns a tuple
        with the length of a string and
        its first character.
    """
    # get the sentence's length using len() method
    length = len(sentence)
    first = sentence[0] if len(sentence) > 0 else None
    return (length, first)
