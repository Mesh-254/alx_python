#!/usr/bin/python3
def multiple_returns(sentence):
    """
        function that returns a tuple
        with the length of a string and
        its first character.
    """
    # get the sentence's length using len() method
    if len(sentence) == 0:
        return None
    return (len(sentence), sentence[0])
