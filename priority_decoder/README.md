# Burgled Again

Oh no! You've been burgled again!

To catch the their, you install a motion sensor. Each minute, the motion sensor
prints either "1" (if there was motion) or "0" (no motion) on a paper tape.
Unfortunately, this format is really difficult to read, so you decide to whip
out your handy Altair 8800 personal computer and it's paper tape reader.

As you feed in the tape, you must write a program to display the number of
minutes since the sensor was powered on at which each motion ("1") event
occurred, this way you can figure out what time you need to lie in wait for the
burglar.


# Input Format

One positive integer number $n$ between $1$ and $2^21$ followed by a newline
- this is the number of lines making up the rest of the list.

$n$ many integers which are either $0$ or $1$, one per line.

# Output Format

Between $0$ and $n$ many positive integers, one per line. Each such integer
must correspond to an index in the input which contains a $1$. The output
integers should be sorted from smallest to largest.

# Samples

## Sample 1

Input:

```
5
1
1
0
1
0
```

Output:

```
0
1
3
```

## Sample 2

Input:

```
10
1
0
1
1
0
1
0
1
1
1
```

Output:

```
0
2
3
5
7
8
9
```
