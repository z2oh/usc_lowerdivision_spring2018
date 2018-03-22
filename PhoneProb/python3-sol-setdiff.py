
import time

start = time.time()

line1 = input().split()
N = line1[0]
K = line1[1]

Nset = set()
Kset = set()

for word in input().split():
	Nset.add(int(word))
for i in range(int(K)):
	Kset.add(int(input()))

listlens = int(N) + int(K)

theset = Nset.union(Kset)

print(listlens - len(theset))

end = time.time()
print("Execution time: {}".format(end-start))
