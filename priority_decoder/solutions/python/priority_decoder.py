#!/usr/bin/env python3

import sys

n = None
i = 0
for line in sys.stdin:
    line = line.strip()
    if n is None:
        # read n, only on the first iteration
        n = int(line)
    else:
        # handle all remaining lines
        if line == '1':
            # if the line is a 1, print the index
            sys.stdout.write(str(i))
            sys.stdout.write("\n")
        i += 1
