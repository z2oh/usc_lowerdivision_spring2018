import time

start_time = time.time()

line1 = input().split()
N_int = int(line1[0])
K_int = int(line1[1])


count = 0

dictlist = input().split()
checklist = []
for i in range(K_int):
	checkword = input();
	for dictword in dictlist:
		if checkword == dictword:
			print(count)
			count += 1
			break

print(count)		
end_time = time.time()
print("Execution time: {}".format(end_time-start_time))


