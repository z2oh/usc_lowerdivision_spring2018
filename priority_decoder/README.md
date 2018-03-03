# Priority Decoder (Name TBD)

**TODO**: fill in background story

# Input Format

One positive integer number $n$ between $1$ and $2^32 -1$ followed by a newline
- this is the length of the following list.

$n$ many integers which are either $0$ or $1$, one per line.

# Outpu Format

Between $0$ and $n$ many positive integers, one per line. Each such integer
must correspond to an index in the input which contains a $1$. The output
integers should be sorted from smallest to largest.

# Samples

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
