#!/usr/bin/env python3

# $1 should be size of image

import sys
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,/?!@#$%^&*()0987654321"
n = int(sys.argv[1])

for i in range(n):
    sys.stdout.write("{}\n".format(' '.join([random.choice(chars) for x in range(n)])))
