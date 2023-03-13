#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    size = len(sentence)
    char = sentence[0]
    return (size, char)
