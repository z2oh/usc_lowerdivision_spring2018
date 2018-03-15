#!/usr/bin/env python3

import sys
import math

# read all lines of input
lines = [x.strip() for x in sys.stdin]

# extract n and k
n = int(lines[0])
k = int(lines[1])

# extract image
image = [x.split() for x in lines[2:]]

# sanity check
assert(k % 90 == 0)

def rot_counterclockwise(i, j):
    # rotate i 90 degrees counterclockwise, j many times

    # initialize the output to be blank
    output = []
    for row in range(n):
        output.append([' ' for x in range(n)])

    if j < 1:
        # base case for recursion where we are asked to rotate 0 times
        return i
    else:
        for row in range(n):
            for col in range(n):
                output[row        ][col        ] = i[col        ][n - 1 - row]
                output[col        ][n - 1 - row] = i[n - 1 - row][n - 1 - col]
                output[n - 1 - row][n - 1 - col] = i[n - 1 - col][row        ]
                output[n - 1 - col][row        ] = i[row        ][col        ]
        if j == 1:
            return output
        else:
            return rot_counterclockwise(output, j-1)

def rot_clockwise(i, j):
    # rotate i 90 degrees clockwise, j many times
    if j < 1:
        return i
    elif j == 1:
        return rot_counterclockwise(i, 3)
    else:
        return rot_clockwise(rot_clockwise(i, 1), j-1)

result = None
if k > 0:
    result = rot_clockwise(image, (k % 360) / 90)
else:
    result = rot_counterclockwise(image, ((-1 * k) % 360) / 90)


for row in range(n):
    sys.stdout.write("{}\n".format(' '.join([x for x in result[row]])))
