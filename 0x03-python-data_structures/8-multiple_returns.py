#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        mt = (0, None)
    else:
        mt = (len(sentence), sentence[:1])
    return(mt)
