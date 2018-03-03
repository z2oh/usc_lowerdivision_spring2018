#!/usr/bin/env bash

FIRST="YES"
I=-2
while read -r line ; do
	# I=$(expr $I + 1)
	# I=$(echo "$I + 1" | bc)
	let I+=1
	if [ $line -eq "1" ] ; then
		echo "$I"
	fi
done
