#!/bin/sh

# make sure we are in the test case directory
cd "$(dirname "$0")"

if [ $# -ne 3 ] ; then
	echo "USAGE: $0 [test case number] [size] [rotation degrees]"
	exit 1
fi

INPUT_FILE="./input/input$1.txt"
OUTPUT_FILE="./output/output$1.txt"

if [ -e "$INPUT_FILE" ] ; then
	echo "ERROR: '$INPUT_FILE' exists"
	exit 1
fi

if [ -e "$OUTPUT_FILE" ] ; then
	echo "ERROR: '$OUTPUT_FILE' exists"
	exit 1
fi

echo "$2"  > "$INPUT_FILE"
echo "$3" >> "$INPUT_FILE"
./generate_image.py $2 >> "$INPUT_FILE"

../solutions/python3/image_rotate.py < "$INPUT_FILE" > "$OUTPUT_FILE"
