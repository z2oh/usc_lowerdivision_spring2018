#!/usr/bin/env python3

# $1 . . . # of lines
import sys
import random

n = int(sys.argv[1])

sys.stdout.write(str(n))
sys.stdout.write("\n")
for i in range(0, n):
    v = random.choice(['1', '0'])
    sys.stdout.write(v)
    sys.stdout.write("\n")
