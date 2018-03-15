#!/bin/sh

BASE="$(dirname "$0")"
TESTCASES="$BASE/../../testcases/"

for testcase in "$TESTCASES"/input/*.txt ; do
	TEST_NUM="$(echo "$(basename "$testcase")" | tr -d [a-zA-Z.])"
	printf "Running test $TEST_NUM... "
	RESULT_FILE="/tmp/$(uuidgen)"
	ERR="$("$BASE/image_rotate.py" < "$testcase" 1> "$RESULT_FILE") 2>&1"
	DIFF="$(diff "$TESTCASES/output/output$TEST_NUM.txt" "$RESULT_FILE")"
	if [ "$(echo "$DIFF" | wc -l)" != "1" ] ; then
		echo "FAIL"
		echo "Difference between output and expected: "
		echo "$DIFF" | while read -r ln ; do
			echo -e "\t$ln"
		done
		echo ""
	else
		echo "PASSED"
	fi
	rm -f "$RESULT_FILE"
done

