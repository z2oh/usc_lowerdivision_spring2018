#! /usr/bin/python3

import argparse
import random

def create_phone_number():
	ran_seed = str(random.randint(100000000000, 1000000000000000))
	len_switcher = random.randint(12,15)
	ran_num = ran_seed[0:len_switcher].zfill(len_switcher)	
	
	res = "+" + ran_num
	# print("Testing... " + res + "  [len=" + str(len(res)-1) +"]")
	return res

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("N")
	parser.add_argument("K")
	parser.add_argument("OutFileName")
	args = parser.parse_args()
	
	N = int(args.N)
	K = int(args.K)
	
	Nlist = []
	Klist = [] # couldn't you use set difference to calculate
	with open(args.OutFileName, "w+") as f:
		f.write(str(N) + " " + str(K) + "\n")
		for i in range(N):
			f.write(create_phone_number())
			if i != N-1:
				f.write(" ")
		f.write("\n")
		for i in range(K):
			f.write(create_phone_number() + "\n")
		
if __name__ == "__main__":
	main()	
