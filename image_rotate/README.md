# ASCII Art Rotation

You've drawn up some beautiful ASCII art! However, you've just realized it
really would be better if it was rotated a bit.

You must scan in your ASCII art, rotate it by a given angle, then display
the output.

# Input Format

The first line will contain a single number $n$.

The second line will contain a single number $k$.

The following $n$ many lines will each contain $n$ many space-delimited
characters. The last $n$ many lines of input are the image to be rotated.

# Output Format

The output should contain $n$ many lines of $n$ characters each. These
characters will represent the input image rotated by $k$ many degrees.

**NOTE**: A positive $k$ means the rotation should be on a clockwise direction.

# Constraints

$2 \leq n \leq 1000$

$k \% 90 = 0$ ($k$ will always be a multiple of 90)

$2^31 -1 \leq k \leq 2^31 -1$
