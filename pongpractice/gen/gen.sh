#!/bin/bash

# Generates Test Cases Randomly, starting at specified number
# Args: ./gen.sh <#Cases> <#Start=0> <Max Width and Length>
# Note that LEN and WID may be up to 2 higher than the MAX Number

if [ $# -eq 0 ]; then
  echo "Usage: <# Cases> <# Start> <Max Width and Length>"
  exit
fi

CASES=$1
START=$2
MAX=$3

if [ "$MAX" -lt 2 ]; then
  echo "Warning: MAX Value Should probably be higher"
fi

if [ "$MAX" -gt 32767 ]; then
  echo "Warning: Parameters will never reach MAX Value, as the max is 32767"
fi

## LEN and WID Start on 2
#LEN=$(expr $(expr $RANDOM % $MAX) + 2)
#WID=$(expr $(expr $RANDOM % $MAX) + 2)
#BS=$(expr $(expr $RANDOM % $WID) + 2)
#BD=$(expr $RANDOM % 2)
#if [ "$BD" -eq 0 ]; then
#  BD="SE"
#else
#  BD="NE"
#fi
#PH=$(expr $RANDOM % $(expr $(expr $WID + 1) / 2) + 1)
#echo "$LEN $WID $BS $BD $PH"

for i in $(seq $START $CASES); do
  # <MAX> <CASE>
  . genInput.sh "$MAX" $i
done
