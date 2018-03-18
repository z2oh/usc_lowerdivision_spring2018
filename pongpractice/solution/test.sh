#!/bin/bash

echo "Testing Solutions..."

LEN=80
WID=40
BS=0
BD="SE"
PH=5

cd java
java Main <<< "$LEN $WID $BS $BD $PH" > test.txt
cd ..

cd python
python Main.py <<< $LEN $WID $BS $BD $PH > test.txt
cd ..


