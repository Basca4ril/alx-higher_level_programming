#!/usr/bin/python3
import hidden_4

names = dir(hidden_4)

fnames = [name for name in names if not name.startswith("__")]
fnames.sort()
for name in fnames:
    print(name)
