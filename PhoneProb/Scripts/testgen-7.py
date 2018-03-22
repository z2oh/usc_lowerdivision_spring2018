#! /usr/bin/python3

import argparse
import random

def create_phone_number_len7(length=7):
	ran_seed = str(random.randint(0, 9999999))

	ran_num = ran_seed.zfill(7)	
	
	res = ran_num
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
		
	Nset = set()
	Kset = set() # couldn't you use set difference to calculate
	
	for i in range(N):
		Nset.add(create_phone_number_len7())
	for i in range(K):
		Kset.add(create_phone_number_len7())
	N_len = len(Nset)
	K_len = len(Kset)
	
	with open(args.OutFileName, "w+") as f:
		f.write(str(N_len) + " " + str(K_len) + "\n")
		for word in Nset:
			f.write(str(word))
			f.write(" ")
		f.write("\n")
		for word in Kset:
			f.write(word + "\n")
		
if __name__ == "__main__":
	main()	
