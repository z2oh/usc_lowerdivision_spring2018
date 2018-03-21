#!/bin/bash

read -a nums;

echo -n "${nums[0]}"
for n in $(seq 2 $(expr "${#nums[@]}" - 1))
do
	echo -n "-$(expr "${nums[$n]}" - 1),$(expr "${nums[$n]}" + 1)"
done
echo "-${nums[1]}"
