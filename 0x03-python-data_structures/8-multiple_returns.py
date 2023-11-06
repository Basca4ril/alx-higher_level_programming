#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (None, None)

    char = sentence[0]
    lenn = len(sentence)

    return (lenn, char)
