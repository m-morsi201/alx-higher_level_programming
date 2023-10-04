#!/usr/bin/python3
for r in range(0,10):
    for c in range(r + 1, 10):
        if r == c:
            pass
        elif r == 8 and c==9:
            print("{}{}".format(r, c))
        else:
            print("{}{}".format(r, c), end=", ")
