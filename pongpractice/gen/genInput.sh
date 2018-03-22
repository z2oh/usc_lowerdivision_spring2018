#!/bin/bash

# Generates a Single Test Case
if [ $# -lt 2 ]; then
  echo "Usage: <MAX#> <CASE #>"
  exit
fi

MAX=$1
CASE=$2

if [ $MAX -eq 2 ]; then
  LEN=2
  WID=2
  BS=$(expr $(expr $RANDOM % $WID))
  BD=$(expr $RANDOM % 2)
  if [ "$BD" -eq 0 ]; then
    BD="SE"
  else
    BD="NE"
  fi
  PH=$(expr $RANDOM % $(expr $(expr $WID + 1) / 2) + 1)
else
  # LEN and WID Start on 2
  LEN=$(expr $(expr $RANDOM % $MAX) + 2)
  WID=$(expr $(expr $RANDOM % $MAX) + 2)
  BS=$(expr $(expr $RANDOM % $WID))
  BD=$(expr $RANDOM % 2)
  if [ "$BD" -eq 0 ]; then
    BD="SE"
  else
    BD="NE"
  fi
  PH=$(expr $RANDOM % $(expr $(expr $WID + 1) / 2) + 1)

fi
echo "Case $CASE: $LEN $WID $BS $BD $PH"

FILE_NUMB="$CASE"
STRLEN=$(echo -n $CASE | wc -m)
if [ $STRLEN -lt 2 ]; then
  FILE_NUMB="0$CASE"
fi

INPUT_FILE="$(pwd)/../testcases/input/input$FILE_NUMB.txt"
OUTPUT_FILE="$(pwd)/../testcases/output/output$FILE_NUMB.txt"

#echo "Files: $INPUT_FILE $OUTPUT_FILE"

if [ -e $INPUT_FILE ]; then
  echo "ERROR: $INPUT_FILE exists! Exiting.."
  exit 1
fi
if [ -e $OUTPUT_FILE ]; then
  echo "ERROR: $OUTPUT_FILE exists! Exiting.."
  exit 1
fi

# Input File
echo | cat > "$INPUT_FILE" << EOF
$LEN
$WID
$BS
$BD
$PH
EOF

# Output File
cd ../solution/java/
java Main <<< "$LEN $WID $BS $BD $PH" > "$OUTPUT_FILE"
cd ../../gen

#echo "Current Directory: $(pwd)"

