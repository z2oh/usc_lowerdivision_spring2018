#!/bin/bash

#LEN=80
#WID=40
#BS=0
#BD="SE"
#PH=5

if [ $# -ne 5 ]; then
  echo "Incorrect Parameters: {LEN, WID, BS, BD, PH}"
  exit
fi

echo "Testing Solutions..."

LEN=$1
WID=$2
BS=$3
BD=$4
PH=$5

echo "Arguments: $LEN $WID $BS $BD $PH"

cd java
java Main <<< "$LEN $WID $BS $BD $PH" > test.txt
cd ..

cd python
python Main.py > test.txt << EOF
$LEN
$WID
$BS
$BD
$PH
EOF
 
cd ..

diff java/test.txt python/test.txt


