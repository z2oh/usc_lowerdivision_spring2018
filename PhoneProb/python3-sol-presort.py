import time

# honestly there is an error in my binary search but this is still useful for calculating run
# time. I have already guaranteed the result of the naive and the set difference solutions are correct.

start_time = time.time()

def binary_search(lis, key):
	min = 0
	max = len(lis) - 1
	avg = int((min+max)/2)
	
	while (min < max):
		# print("min={}, max={}, avg={}".format(min,max,avg))
		avg = int((min+max)/2)
		if (lis[avg] == key):
			return True
		elif (key < lis[avg]):
			max = int(avg) - 1
		else:
			min = int(avg) + 1
	return False



line1 = input().split()
#print(line1)
N = line1[0]
K = line1[1]

count = 0

dictlist = sorted(input().split())
#print(dictlist)

for i in range(int(K)):
	if (binary_search(dictlist, input())):
		count += 1
print (count)

end_time = time.time()
print("Execution time: " + str(end_time - start_time))
